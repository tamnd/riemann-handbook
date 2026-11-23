---
id: integral-connection-taylor-formula-tame-breuil-kisin
title: An integral connection with a Taylor formula on a tame Breuil-Kisin module, a second name
kind: theorem
decl: GlobalTheory.T.integralConnection_taylorFormula_tameBreuilKisin
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.IntegralConnectionTaylorFormulaTameBreuilKisinStatement
covers: 437
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`IntConnTaylor.main`](/entry/int-conn-taylor-main/), which has the proof. It is step 2 of [a tame Breuil-Kisin module for each good lattice](/entry/exists-pack-is-of-type/): it gives the connection of the pack.

## Statement

The setting is that of [the parent entry](/entry/exists-pack-is-of-type/), with $\ell \ne 2$ and the tame field $K_\varpi$. Let $P$ be a $\varphi$-module over power series (`PhiMod`), $T$ a lattice of $G_{\mathbb{Q}_\ell}$, and $I$ an identification of $P$ with $T$ over Witt vectors (`Ident`).

Two objects come with $P$:

- the ring $S$ of power series $\sum_n c_n X^n$ over $L$ with $|c_n|\,|\lfloor n/e \rfloor!| \le 1$ and $|c_n|\,|\lfloor n/e \rfloor!| \to 0$, and the $S$-span $M_S$ of the columns of the matrices of $P$ (`P.MM`);
- the operator $\nabla_P$ (`P.nabla`): the derivative $d/dX$, conjugated by the matrix of the unique Frobenius-compatible section `xiExt`.

A *connection* on $P$ (`Conn`) is an operator $\nabla$ with the Leibniz rule $\nabla(fv) = f'v + f\nabla v$ that maps $M_S$ into $M_S$. Put $N = X\nabla$. The connection satisfies the *Taylor formula* (`Ident.Taylor`) if for each $g \in G_{K_\varpi}$, with $\Gamma_g$ the matrix of $g$ on the lattice, and each $m \in M_S$,

$$\Gamma_g \cdot g(m) = \sum_{i \ge 0} \mu_g^{[i]}\, N(N-1)\cdots(N-i+1)\, m,$$

with $\ell$-adic convergence in a crystalline period ring. Here $\mu_g^{[i]}$ is the $i$-th divided power of an element $\mu_g$ attached to $g$ and $\varpi$.

**Theorem.** Assume `BhattScholzeCrystallineLattices`. If the restriction of $I$ to $G_{K_\varpi}$ comes from a prismatic F-crystal (`IsBK`), then $\nabla_P$ is a connection on $P$ (it maps $M_S$ into $M_S$), and it satisfies the Taylor formula.

The ring $S$ has the shape of the divided power ring of Breuil (*Groupes $p$-divisibles, groupes finis et modules filtrés*, Ann. of Math. 152, 2000).

## Proof

The proof is `exact IntConnTaylor.main`. [That entry](/entry/int-conn-taylor-main/) describes the proof: an integral stratification matrix from the F-crystal, whose coefficients are the powers of $\nabla_P$.

## In the Lean code

The theorem is in [IntegralConnectionTaylorFormulaTameBreuilKisinStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IntegralConnectionTaylorFormulaTameBreuilKisinStatement.lean#L10). `Conn` and `Ident.Taylor` are in [ExistsIterateDerivative.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ExistsIterateDerivative.lean#L602), and $S$ in [NormPowLeNormFactorial.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/NormPowLeNormFactorial.lean#L132).

- The conclusion is stated as "there is a connection $C$ with $C.\nabla = \nabla_P$". A `Conn` is determined by its operator, so the content is that $\nabla_P$ preserves $M_S$, and the Taylor formula.
- We did not unfold `toCris`, the ring `OCr` or the element `ϖ.mu g`.
