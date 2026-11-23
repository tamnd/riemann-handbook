---
id: int-conn-taylor-main
title: The connection of a Breuil-Kisin module is integral and gives the Galois action
kind: theorem
decl: GlobalTheory.IntConnTaylor.main
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.IntegralConnectionTaylorFormulaTameBreuilKisin
covers: 436
status: drafted
drafted_by: writer@claude
---
This theorem shows that the canonical connection of a Breuil-Kisin module preserves its divided power lattice, and that $G_{K_\varpi}$ acts on the Galois lattice by the Taylor series of this connection. It is the proof behind the second name [`integralConnection_taylorFormula_tameBreuilKisin`](/entry/integral-connection-taylor-formula-tame-breuil-kisin/), which step 2 of [`exists_pack_isOfType`](/entry/exists-pack-is-of-type/) uses to build the connection of a pack.

## Statement

The setting is that of [`exists_pack_isOfType`](/entry/exists-pack-is-of-type/): a prime $\ell \ne 2$, a coefficient field $L$, a system of roots $\varpi$ and the tame field $K_\varpi$. Let $P$ be a $\varphi$-module of rank $n$: invertible matrices $Y_\tau$ over $\mathcal{O}_L[[X]][1/E]$ for $\tau \in \mathbb{Z}/a$, with $E = X^e + \ell$, and $\varphi(v)_\tau = Y_\tau \,\mathrm{Frob}(v_{\tau-1})$. Let $M$ be the standard lattice over $\mathcal{O}_L[[X]]$, and $\varphi^* M$ the span of $\varphi(M)$, that is, of the columns of the $Y_\tau$.

Let $S$ be the ring of series $\sum c_k X^k$ in $L[[X]]$ with $|c_k| \cdot |\lfloor k/e \rfloor !| \le 1$ and tending to $0$. Let $S\varphi^*M$ (`MM`) be the $S$-span of $\varphi^* M$.

The *canonical connection* of $P$ (`PhiMod.nabla`) is $\nabla = \xi \circ \frac{d}{dX} \circ \xi^{-1}$, where $\xi_\tau$ is the matrix with constant term $1$ that solves $Y_\tau \,\mathrm{Frob}(\xi_{\tau-1}) = \xi_\tau\, Y_\tau(0)$ (a limit of iterates, `xiSeq`). A *connection* on $P$ (`Conn`) is a map that satisfies the Leibniz rule and preserves $S\varphi^*M$. Put $N = X\nabla$.

**Theorem.** Assume `BhattScholzeCrystallineLattices`. Let $T$ be a lattice of $G_{\mathbb{Q}_\ell}$ and $I$ an identification of $P$ with $T$ over Witt vectors (`Ident`) whose restriction to $G_{K_\varpi}$ comes from a prismatic F-crystal (`IsBK`). Then $\nabla$ is a connection on $P$, and it has the Taylor property (`Ident.Taylor`): for each $g \in G_{K_\varpi}$ there is a matrix $\Gamma$ of $g$ on the lattice of $I$ such that, for $m \in S\varphi^*M$,

$$g(m) = \sum_{i \ge 0} \gamma_i(\mu(g))\; N(N-1)\cdots(N-i+1)\, m$$

as an $\ell$-adic limit in the crystalline period ring. Here $\gamma_i$ is the $i$-th divided power, and $g(X^k) = (1 + \mu(g))^k X^k$ in the period ring.

## Proof

1. `exists_taylorShift_frobenius_twoVariable_compatible` gives the Taylor shift $f(X) \mapsto f(X + Y)$ into $L[[X]][[Y]]$, with $i!\,[Y^i] f(X+Y) = f^{(i)}$, and a Frobenius on $L[[X]][[Y]]$ that commutes with it.
2. `exists_integral_crystal_stratification_matrix` (uses `BhattScholzeCrystallineLattices`, $\ell \ne 2$ and `IsBK`) gives matrices $\varepsilon_\tau$ over $L[[X]][[Y]]$ with $\varepsilon_\tau = 1$ at $Y = 0$, a Frobenius relation with the $Y_\tau$, and $k!\,[Y^k]\varepsilon_\tau$ in $S$ for all $k$: an integral stratification.
3. `frobeniusStratification_coeff_eq_connection_pow` identifies $n!\,[Y^n]\varepsilon_\tau$ with the coordinates of $\nabla^n \varphi(e_j)$ in the columns of $Y_\tau$. So $\nabla^n \varphi(e_j) \in S\varphi^*M$ for all $n$.
4. Since $\varphi(e_j) \in S\varphi^*M$ and $S$ is stable under $d/dX$, the Leibniz rule (`nabla_mem_MM_of_basis`) shows that $\nabla$ preserves $S\varphi^*M$.
5. So $X^k$ times the coordinates of $\nabla^k \varphi(e_j)$ lie in $S$. With these coefficients, `galois_dividedTaylor_expansion_frobeniusBasis` (uses `BhattScholzeCrystallineLattices`) writes $\Gamma$ as a divided power series in $\mu(g)$. `galois_taylor_formula_breuilKisin_lattice` turns this into the Taylor property, through $X^k \frac{d^k}{dX^k} = N(N-1)\cdots(N-k+1)$.

## In the Lean code

The theorem is in [IntegralConnectionTaylorFormulaTameBreuilKisin.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IntegralConnectionTaylorFormulaTameBreuilKisin.lean#L16). `PhiMod` and `MM` are in [PowerSeriesVecReduceModUMulVec.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/PowerSeriesVecReduceModUMulVec.lean#L72), $S$ in [NormPowLeNormFactorial.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/NormPowLeNormFactorial.lean#L132), $\nabla$ and $\xi$ in [ConnPhiExtensionGeneratorEqZeta.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ConnPhiExtensionGeneratorEqZeta.lean#L302), and `Conn` and `Taylor` in [ExistsIterateDerivative.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/ExistsIterateDerivative.lean#L602). The five lemmas of the proof are imported from "Statement" files; we did not open their proofs, nor `IsLMat`, `toCris` and `mu`.

The Lean conclusion is "there is $C$ with $C.\nabla = \nabla$": no new connection is built, and $C$ is $\nabla$ with the proof of step 4 attached. Steps 2 and 5 are the only uses of `BhattScholzeCrystallineLattices`.
