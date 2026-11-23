---
id: ss-pot-b-at-newform
title: A Hecke projector on potentials at a newform eigensystem
kind: theorem
decl: GlobalTheory.KZ.SSPotBr.ssPotB_at_newform
module: Development.AbelianVarietyTheory.Proofs.FoundationProofs.SemisimplePotentialsAtNewformEigensystem
covers: 922
status: drafted
drafted_by: writer@claude
---
This theorem gives a Hecke polynomial $P$ that projects polynomial valued potentials of level $\Gamma_1(N) \cap \Gamma_0(\ell)$ onto the eigensystem $\lambda$ of a newform $g$, up to trivial terms. It is restated as [the second name](/entry/semisimple-potentials-at-newform-eigensystem/), which [the Hecke projector for a newform](/entry/hecke-proj-newform/) uses to get $\mathrm{SSPotB}$ at weight $w = k - 2$.

## Statement

The data $k, g, N, \ell, \alpha, \lambda$ and their conditions are those of [the second name](/entry/semisimple-potentials-at-newform-eigensystem/). Let $\Gamma = \Gamma_1(N) \cap \Gamma_0(\ell)$, let $\mathcal{H}$ be the upper half plane, and let $\mathbb{C}[X_0, X_1]_w$ be the homogeneous polynomials of degree $w$, with the right action $p|\gamma$ by linear substitution.

- A *potential* of weight $w$ is a map $F \colon \mathbb{C} \to \mathbb{C}[X_0, X_1]_w$ such that for each $\gamma \in \Gamma$ the function $F(\gamma z)|\gamma - F(z)$ is constant on $\mathcal{H}$.
- A potential is *trivial* if $F = \psi + p$ on $\mathcal{H}$, with $\psi$ invariant ($\psi(\gamma z)|\gamma = \psi(z)$) and $p$ a constant polynomial.
- The letters act by $T_q = \sum_{j<q} [\begin{smallmatrix}1&j\\0&q\end{smallmatrix}] + \sigma_q [\begin{smallmatrix}q&0\\0&1\end{smallmatrix}]$, $U = \sum_{j<\ell}[\begin{smallmatrix}1&j\\0&\ell\end{smallmatrix}]$ and $\langle d \rangle = \sigma_d$, where $\sigma_d \in \mathrm{SL}_2(\mathbb{Z})$ is a chosen diamond matrix and each matrix $m$ acts by $F \mapsto F(mz)|m$. The admitted letters are $T_q$ for primes $q \nmid N\ell$, $U$, and $\langle d \rangle$ for $d$ prime to $N$.

**Theorem.** There is a noncommutative polynomial $P$ in the admitted letters with $\lambda(P) = 1$ such that $(T - \lambda(T))PF$ is trivial for each potential $F$ of weight $k-2$ and each admitted letter $T$.

## Proof

Let $Z^1$ be the cocycles $z \colon \Gamma \to \mathbb{C}[X]_{\le w}$ with $z(\gamma\delta) = z(\gamma)|\delta + z(\delta)$, and $B^1$ the coboundaries $\gamma \mapsto p|\gamma - p$. The quotient is the Eichler-Shimura cohomology.

1. **Hecke operators on cocycles.** `heckeOperatorOnCocycleMaps_cocycle_coboundary_conj` shows that the cocycle versions of the admitted letters preserve $Z^1$ and $B^1$. It uses the coset representatives of `heckeDoubleCosetReps_gammaOneGammaZeroLevel`.
2. **Commutation.** `heckeDiamond_commute_mod_coboundaries_gamma1Gamma0` shows that the letters commute modulo $B^1$. For pairs without a $T_q$, the proof feeds the lemma a dummy prime $q_0 > N\ell$.
3. **Semisimplicity.** `hecke_semisimple_generalised_eigen_newform_gamma1Gamma0` says: if $(T - \lambda(T))^n z \in B^1$ for every admitted $T$, then $(T - \lambda(T))z \in B^1$. So the generalized $\lambda$-eigenspace equals the $\lambda$-eigenspace modulo $B^1$. This is where the conditions on $\alpha$ enter. The first one says that $\alpha$ is not the other root of the Hecke polynomial at $\ell$.
4. **The polynomial.** $Z^1$ has finite dimension (`eichlerShimuraCocycles_gammaOneGammaZero_finiteDimensional`). `exists_joint_genEigenspace_idempotent_poly`, a statement of linear algebra, then gives $P$ with $\lambda(P) = 1$ that maps $Z^1$ into the $\lambda$-eigenspace modulo $B^1$.
5. **Back to potentials.** The map $F \mapsto (\gamma \mapsto F(\gamma z)|\gamma - F(z))$ sends potentials to $Z^1$. By `letter_pot` and `lift_pot`, it intertwines the two actions of each polynomial. By `potentialCocycleDehomogenised_laws`, it is linear, and a potential whose cocycle is in $B^1$ is trivial. Step 4 then gives the theorem.

## In the Lean code

The theorem is in [SemisimplePotentialsAtNewformEigensystem.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/SemisimplePotentialsAtNewformEigensystem.lean#L101), with `letter_pot` and `lift_pot` in the same file. $\mathrm{SSPotB}$ is in [LiftApplyOfMemAdmissibleSubalgebra.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/LiftApplyOfMemAdmissibleSubalgebra.lean#L14), and the potentials, trivial potentials and letter operators are in [OpLDOneSubMemTriv.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/OpLDOneSubMemTriv.lean#L14). The semisimplicity theorem is in [HeckeSemisimpleGeneralisedEigenNewformGamma1GammStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/HeckeSemisimpleGeneralisedEigenNewformGamma1GammStatement.lean#L8); it restates `HeckeFamilyMatrices.hecke_semisimple_at_newform`, whose proof we have not opened.

A potential is a function on all of $\mathbb{C}$, and the conditions are asked only on $\mathcal{H}$; no holomorphy is asked. The trivial part $\psi$ need not be homogeneous. The definition `SSPot` in [OpLDOneSubMemTriv.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/OpLDOneSubMemTriv.lean#L43) is the same as `SSPotB` under another name.
