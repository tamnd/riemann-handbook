---
id: wgl-g-tlower-of
title: Integral branching maps for interlacing weights, from four facts on Weyl modules
kind: theorem
decl: PI.WGL.gTLower_of
module: Formalism.PeriodIntegrals.UnitaryGroupMassFormula.GelfandTsetlinLowering.GTLowerOf
covers: 402
status: drafted
drafted_by: writer@claude
---
This theorem proves `GTLower`. For a dominant weight $\lambda$ of $\mathrm{GL}_N$ and a weight $\sigma$ of $\mathrm{GL}_{N-1}$ that interlaces it, it gives an equivariant map $\iota$ from the model of $\sigma$ into the model of $\lambda$, and a map $\beta$ back, both integral and with an explicit bound in the Fock norm. It takes four facts on Weyl modules as hypotheses and assembles eight proved steps. Its caller [`gTLower_of`](/entry/g-tlower-of/) fills in the four facts and sets up the notation that we use here.

## Statement

Let $\lambda$ be dominant for $\mathrm{GL}_N$ and $\sigma$ dominant for $\mathrm{GL}_n$, $n+1 = N$, with $\lambda_{i+1} \leq \sigma_i \leq \lambda_i$. The code defines from $\lambda$ and $\sigma$:

- an integer $c = c_{\mathrm{Br}}(\lambda,\sigma)$, a product of terms $(v - i) - \sigma_j + j$ over $v$ in the ranges $[\lambda_{i+1}, \min(\lambda_i, \lambda_{i+1} + D_0)]$ with $v \neq \sigma_i$, where $D_0 = \sum_i (\sigma_i - \lambda_{i+1})$;
- a polynomial $\xi = \prod_i m_{i+1}^{\sigma_i - \lambda_{i+1}} \, m'_i{}^{\lambda_i - \sigma_i}$, where $m_{i+1}$ is the leading principal minor of size $i+1$ and $m'_i$ is the minor on rows $0, \dots, i-1$ and $N-1$;
- bounds $c_{\mathrm{Bd}}$ and $b = c_{\mathrm{Bd}} \sqrt{\dim \Delta_{\mathbb C}(\lambda)}$.

The hypotheses are `FactDelDualNabla` (see the caller), and:

- `HwIrred`: $\nabla_{\mathbb C}(\lambda) = \Delta_{\mathbb C}(\lambda)$, it is irreducible, and its vectors fixed by the upper unitriangular group are the multiples of the extremal vector;
- `GTBranch`: the restriction of $\nabla(\lambda)$ to $\mathrm{GL}_n$ is the sum of the images of $\nabla(\mu)$ over interlacing $\mu$, each with multiplicity one;
- `SchurFock`: if $\lvert s \rvert \leq 1$ on $U(N)$, then $\langle s, s \rangle_\lambda \leq \dim \Delta(\lambda)$.

**Theorem.** Then $c \neq 0$, $\lvert c \rvert \leq c_{\mathrm{Bd}}$, $\xi \neq 0$, the weight $\sum \lambda - \sum \sigma$ of the last diagonal torus equals $\lambda_0 - D_0$, and there are maps $\iota$ and $\beta$. The map $\iota$ is $\mathrm{GL}_n$-equivariant, sends $\nabla_{\mathbb Z}(\sigma)$ into $\nabla_{\mathbb Z}(\lambda)$, sends the extremal vector to $c\,\xi$, and satisfies $\langle \iota s, \iota s \rangle_\lambda \leq b^2 \langle s, s \rangle_\sigma$. The map $\beta$ is its adjoint for the Fock pairings, sends $\Delta_{\mathbb Z}(\lambda)$ into $\Delta_{\mathbb Z}(\sigma)$, and has the same bound.

## Proof

The arithmetic facts on $c$ and the facts on $\xi$ (`Numbers`, `XiFacts`) are proved without hypotheses. Then:

1. `ioExists_of`: there is an equivariant $\iota_0$ with $\iota_0(\text{extremal}) = \xi$. It uses `HwIrred` and `GTBranch`.
2. `ioIntegral_of`: $c\,\iota_0$ is integral. `CapelliZ` gives an integral operator $Z$ that acts on each image of $\nabla(\mu)$ by an integer $z(\mu)$, with $z(\sigma) = c$ by definition. `ZScalarVanish` gives $z(\mu) = 0$ for the other $\mu$ of the same total degree. `LiftMod` lifts $\iota_0(s)$ to an integral $m$ modulo those other images. So $c\,\iota_0(s) = Z(m)$ is integral.
3. `adjointBr_of`: $\beta(f) = \sum_k \langle f, \iota b_k \rangle_\lambda \, b_k$ for a frame $(b_k)$ of $\nabla(\sigma)$. By irreducibility $\beta \circ \iota$ is a scalar. So $\langle \iota s, \iota s \rangle = \lvert c \rvert^2 \langle \xi, \xi \rangle \langle s, s \rangle$, and `SchurFock` applied to $\xi$ gives the bound $b^2$.
4. `brIntegral_of`: $\beta$ is integral, by `FactDelDualNabla` and `HwIrred`.
5. `gTLower_of_steps` sets $\iota = c\,\iota_0$ and collects the clauses.

`GTBranch` is the classical branching rule from $\mathrm{GL}_N$ to $\mathrm{GL}_{N-1}$; see Goodman and Wallach, *Symmetry, Representations, and Invariants*, Chapter 8. We have not unfolded `liftMod_of` or `brIntegral_of` beyond their hypotheses.

## In the Lean code

The theorem is in [GTLowerOf.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/GelfandTsetlinLowering/GTLowerOf.lean#L14). The step statements are in [ZScalarVanish.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/GelfandTsetlinLowering/ZScalarVanish.lean#L24). `ioIntegral_of` and `gTLower_of_steps` are in [Assembly.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/GelfandTsetlinLowering/Assembly.lean#L10), and `adjointBr_of` in [ConstructionAdj.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/GelfandTsetlinLowering/ConstructionAdj.lean#L13). All four hypotheses are proved in the code, by `factDelDualNabla`, `highest_weight_irreducible`, `gelfand_tsetlin_branching` and `schur_fock`.
