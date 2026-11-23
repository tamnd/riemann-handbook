---
id: fixed-mem-span
title: Invariants of the integral unitary group lie in the span of the vacuum orbit
kind: theorem
decl: GlobalTheory.Hk3.HoweDuality.fixed_mem_span
module: Development.AbelianVarietyTheory.Proofs.SatakeParameters.RhoMemOfMkEq
covers: 362
status: drafted
drafted_by: writer@claude
---
This theorem is clause 2 of the unramified Howe statement. [howe-unram-holds](/entry/howe-unram-holds/) uses it twice: once directly, and once for the swapped pair to get clause 1. The notation is the notation of that entry.

## Statement

Take the data of a `LocPair`, a vacuum vector $s \neq 0$, and suppose that the vectors $\rho(x)s$ span $M$. Let $K_T$ be the group of integral elements of $U(J_T)$. If $w \in M$ is fixed by $\omega(1, k)$ for every $k \in K_T$, then $w$ lies in
$$S = \operatorname{span}\{\omega(g, 1)s : g \in U(J_S)\}.$$

## Proof

Write $X = \mathrm{Mat}_{n' \times n}(L)$ and $X_0 = \mathrm{Mat}_{n' \times n}(\mathcal O)$. For a class $c \in X/X_0$, let $V_c$ be the span of the $\rho(x)s$ with $x \in c$.

1. Each $V_c$ lies in a line. If $x - y$ is integral, then $\rho(x)s$ is a nonzero multiple of $\rho(y)s$. This is `rho_mem_of_mk_eq`. It follows from the cocycle rule and $\rho(u)s = s$.
2. The $V_c$ are independent (`latticeModel_vacuumTranslate_classes_independent`), and their sum is $M$ by the span hypothesis.
3. $K_T$ acts on $X/X_0$ by left multiplication, and $\omega(1,k)\rho(x)s = \rho(kx)s$ (`om_rho`). So $\omega(1,k)$ maps $V_c$ into $V_{kc}$.
4. Let the height of $c$ be $\mu(c) = [x\mathcal O^n + \mathcal O^{n'} : \mathcal O^{n'}]$ for $x \in c$. It is well defined and $K_T$-invariant by `matrixLatticeIndex_integral_translation_invariance`.
5. Every vector of $S$ is fixed by $K_T$, because $\omega(1,k)$ and $\omega(g,1)$ commute and $\omega(1,k)s = s$ by the field `fix`.
6. Fix a class $c = x + X_0$. Suppose that the sum of the $V_{kc}$, $k \in K_T$, contains a nonzero $K_T$-fixed vector. Then [howe-duality-step](/entry/howe-duality-step/) gives $v \in S$ and $u$ in the classes of smaller height, such that $v - u$ is nonzero and lies in that orbit sum.

These six facts are the hypotheses of the abstract lemma `invariant_mem_of_orbit_height_separation`. The lemma concludes that every $K_T$-fixed vector lies in $S$. We read its statement only, not its proof `fixed_mem_of_orbit_height`. Its form suggests an induction on the height, but we did not check this.

## In the Lean code

The theorem is in [RhoMemOfMkEq.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/RhoMemOfMkEq.lean#L145). The helper lemmas `rho_add_int`, `rho_mem_of_mk_eq` and `om_rho` are in the same file, at lines 79, 86 and 96. The abstract lemma is stated in [FixedMemOfOrbitHeightStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/FixedMemOfOrbitHeightStatement.lean#L5). The height is `latIdx`, in [MemIntMat.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/MemIntMat.lean#L27). The proof takes $\mu(c)$ as `latIdx` of a chosen representative `Quotient.out c`, and step 4 shows that the choice does not matter.
