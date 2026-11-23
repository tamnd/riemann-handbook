---
id: sw-at-succ
title: The Siegel-Weil step from degree N to degree N plus one, by a Hecke contraction
kind: theorem
decl: GlobalTheory.SW.swAt_succ
module: Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation.SiegelWeilFormulaDegreeSucc
covers: 423
status: drafted
drafted_by: writer@claude
---
This theorem is the real proof of the induction step [siegel-weil-formula-degree-succ](/entry/siegel-weil-formula-degree-succ/), which is only a second name for it. The step feeds the induction in [siegel-weil-definite](/entry/siegel-weil-definite/). The idea: a Hecke relation at a split prime makes a weighted bound on the Siegel-Weil difference smaller by a fixed factor $\theta < 1$, so the difference is zero.

## Statement

Let $E$ be a CM field with a CM type $\Psi$. Let $n$ be even and let $4(N+1) < n$. If `SWAt Ψ n N` holds, then `SWAt Ψ n (N+1)` holds. The entry [siegel-weil-definite](/entry/siegel-weil-definite/) explains `SWAt`.

## Proof

Fix $M$, $R$, an admitted family $\varphi$ of degree $N+1$, and $Z$ in the Hermitian upper half space. Let $D(\mathfrak{X}, Z)$ be the Siegel-Weil difference `swd` of the twisted family `twist R 𝔛 φ`, for a lattice $\mathfrak{X} \subset E^{N+1}$ that agrees with the standard lattice $L_0$ away from $RM$. Let $g(\mathfrak{X}) = [\mathfrak{X} : \mathfrak{X} \cap L_0] / [L_0 : \mathfrak{X} \cap L_0]$ (this is `gidx`), and let $\delta(Z)$ be the product over $\tau \in \Psi$ of the determinants of the imaginary parts (`detIm`). Write $n = 2k$.

1. The hypothesis `SWAt Ψ n N` gives a constant $C$ with $g(\mathfrak{X})^k \lvert D(\mathfrak{X}, Z)\rvert \delta(Z)^k \le C$ for all $\mathfrak{X}$ and $Z$. This is `twisted_siegelWeil_difference_bounded`. I have not unfolded its proof `twist_swd_bounded`.
2. Choose a prime $q$ and a prime ideal $P$ of norm $q$ with $q$ prime to $RM$, $P$ prime to its conjugate, and $q \nmid 2\,\mathrm{disc}(E)$.
3. The Hecke relation at $P$ (`hecke_swd`) writes $(q^{N+1}-1)(q^n+q^{N+1}) D(\mathfrak{X}, Z)$ as $(q-1)$ times a sum of $q^n D(\mathfrak{X}_A, Z)$ and $D(\mathfrak{X}_B, Z + \beta)$. Here $g(\mathfrak{X}_A) = q\,g(\mathfrak{X})$, $q\,g(\mathfrak{X}_B) = g(\mathfrak{X})$, and $\beta$ is Hermitian, so $\delta(Z+\beta) = \delta(Z)$. The relation uses a neighbour count: the $P$-neighbours of a lattice number $(q^n-1)/(q-1)$.
4. Put the bound $S$ into the right side. This gives `bound_step`: the bound $S$ becomes $\theta S$ with $\theta = q^k(1+q^{N+1})/(q^{2k}+q^{N+1})$.
5. $\theta < 1$ because $(q^k - q^{N+1})(q^k - 1) > 0$, which needs $N + 1 < k$.
6. By induction on $m$ the bound is $\theta^m C$. As $m \to \infty$ it goes to $0$. At $\mathfrak{X} = L_0$ we have $g = 1$ and $\delta(Z) > 0$, so $D(L_0, Z) = 0$.
7. On the self-dual lattices, `twist R L₀ φ` equals $\varphi$, so the Siegel-Weil difference of $\varphi$ is zero.

The Lean code cites no source for this contraction argument.

## In the Lean code

The theorem is at [SiegelWeilFormulaDegreeSucc.lean](lean:Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/SiegelWeilFormulaDegreeSucc.lean#L242). The helpers in the namespace `GlobalTheory.SW.Step` of the same file are `swd_nb` (L73), `hecke_swd` (L115) and `bound_step` (L170). Outside lemmas:

- `GlobalTheory.T.twisted_siegelWeil_difference_bounded`, proved by `twist_swd_bounded` in [TwistedSiegelWeilDifferenceBounded.lean](lean:Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/TwistedSiegelWeilDifferenceBounded.lean#L136).
- `GlobalTheory.T.exists_good_split_prime_cmField` and `GlobalTheory.T.hecke_relation_admissibleFamily_pointwise`.
- `twist_admissible` and `Base.classSum_congr` for the last step.

`gidx`, `twist`, `Nb` and `GoodPrime` are in [FirstCoordinateAdmissible.lean](lean:Development/AbelianVarietyTheory/Definitions/SpanningFamilies/FirstCoordinateAdmissible.lean#L154).
