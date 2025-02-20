# Reliable extrapolation of deep neural operators informed by physics or sparse observations

The data and code for the paper [M. Zhu, H. Zhang, A. Jiao, G. E. Karniadakis, & L. Lu. Reliable extrapolation of deep neural operators informed by physics or sparse observations. *Computer Methods in Applied Mechanics and Engineering*, 412, 116064, 2023](https://doi.org/10.1016/j.cma.2023.116064).


## Datasets

- [Diffusion-reaction equation](data/diffusion_reaction)
- [Burgers’ equation](data/burgers)
- [Advection equation](data/advection)
- [Poisson equation](data/poisson)
- [Cavity flow](data/cavity_flow)

To get complete datasets, run data_gen.py and data_gen_low_fidelity.py in the [data](data) folder for each equation.

## Code

- [Diffusion-reaction equation](src/diffusion_reaction)
- [Burgers’ equation](src/burgers)
- [Advection equation](src/advection)
- [Poisson equation](src/poisson)
- [Cavity flow](data/cavity_flow)

## Cite this work

If you use this data or code for academic research, you are encouraged to cite the following paper:

```
@article{zhu2023reliable,
  title   = {Reliable extrapolation of deep neural operators informed by physics or sparse observations},
  author  = {Zhu, Min and Zhang, Handi and Jiao, Anran and Karniadakis, George Em and Lu, Lu},
  journal = {Computer Methods in Applied Mechanics and Engineering},
  volume  = {412},
  pages   = {116064},
  year    = {2023},
  doi     = {https://doi.org/10.1016/j.cma.2023.116064}
}
```

## Questions

To get help on how to use the data or code, simply open an issue in the GitHub "Issues" section.
