import os

# os.environ["DDE_BACKEND"] = "tensorflow.compat.v1"
import numpy as np
import deepxde as dde
from deepxde.backend import tf

dde.config.set_default_float("float16")
tf.keras.mixed_precision.set_global_policy("mixed_float16")


def gelu(x):
    return (
        0.5
        * x
        * (
            1
            + tf.math.tanh(
                tf.cast(tf.math.sqrt(2 / np.pi), tf.float16) * (x + 0.044715 * x**3)
            )
        )
    )


def main():
    ls_train = 0.5
    ls_test = 0.5
    lr = 0.001
    iterations = 500000
    train_data = np.load(f"../../../data/poisson/poisson_train_ls_{ls_train}_5082.npz")
    test_data = np.load(f"../../../data/poisson/poisson_test_ls_{ls_test}_5082.npz")
    X_train = (
        np.repeat(train_data["X_train0"], 5082, axis=0).astype(np.float16),
        np.tile(train_data["X_train1"], (1000, 1)).astype(np.float16),
    )
    y_train = train_data["y_train"].reshape(-1, 1).astype(np.float16)
    X_test = (
        np.repeat(test_data["X_test0"], 5082, axis=0).astype(np.float16),
        np.tile(test_data["X_test1"], (100, 1)).astype(np.float16),
    )
    y_test = test_data["y_test"].reshape(-1, 1).astype(np.float16)
    data = dde.data.Triple(
        X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test
    )

    net = dde.maps.DeepONet(
        [101, 100, 100, 100],
        [2, 100, 100, 100],
        {"branch": "relu", "trunk": gelu},
        "Glorot normal",
    )

    model = dde.Model(data, net)
    model.compile(
        "adam",
        lr=lr,
        metrics=["l2 relative error"],
        decay=("inverse time", iterations // 5, 0.5),
        loss="mean l2 relative error",
    )

    checker = dde.callbacks.ModelCheckpoint(
        "model/model.ckpt", save_better_only=False, period=10000
    )
    losshistory, train_state = model.train(
        iterations=iterations,
        callbacks=[checker],
        batch_size=30000,
        display_every=10,
    )
    dde.saveplot(losshistory, train_state, issave=True, isplot=False)


if __name__ == "__main__":
    main()
