---
id: cm-diff-definite
title: The degree difference of the two Lie eigenlattices of a definite CM object
kind: theorem
decl: GlobalTheory.FlatCore.CMDiff0.cmDiff_definite
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.CmObjectDefiniteLieEigenLatticeDegreeDifference
covers: 342
status: drafted
drafted_by: writer@claude
---
This theorem computes the degree difference of two Lie eigenlattices of a CM object of signature $(p, 0)$. It is the real content behind its second name [cmObject_definite_lieEigenLattice_degree_difference](/entry/cm-object-definite-lie-eigen-lattice-degree-difference/), which [degLie_core_alt](/entry/deg-lie-core-alt/) uses. Below this theorem are 342 declarations.

## Statement

The statement is the one in the [second-name entry](/entry/cm-object-definite-lie-eigen-lattice-degree-difference/). Write $\bar\tau = \tau \circ \bar{\ }$, $L = L_\tau$ and $\bar L = L_{\bar\tau}$. With $q = 0$ and $\tau(\mathrm{rt}) = \rho$, the theorem says
$$\deg_h L - \deg_h \bar L = \frac{p}{2}\,\operatorname{Re}\log\Omega(E,\chi).$$

## Proof

The proof finds a sublattice of each eigenlattice whose degree is known, and then corrects by the index.

1. Substitute $q = 0$. Take generic fibres $F_b$ of the two abelian schemes $A_b$ of $X$, and the tangent maps $M_j$ of the maps $\varphi_j : A_{\mathrm{true}} \to B$ (`DiffCoord.existsUnique_isDiffOf`).
2. Take the Gram matrices $g_P$ (size $p$) and $g_Q$ (size $0$) of the Weil pairings (`T.exists_gramMatrices_cmUnitaryShimuraObject`). Since $g_Q$ is empty, $\det g_Q = 1$.
3. Let $N \subseteq L$ be the sum of the images of the $\tau$-eigenlattices of $F_{\mathrm{true}}$ under the $M_j$ (`subP`), and let $\bar N \subseteq \bar L$ be the analogue for $F_{\mathrm{false}}$ (`subQ`). The lemma `T.cmDefinite_lieIndex_ideal_eq_norm_ideal` gives an ideal $\mathfrak n$ of $\mathcal{O}_E$ with $\mathfrak n \bar{\mathfrak n} = (\det g_P)$ and $\mathrm{idx}(L, N) = \tau(\mathfrak n)\mathcal{O}_K$. This step uses `IsHostField H`. The index $\mathrm{idx}(\bar L, \bar N)$ is the colon ideal of zeroth exterior powers, which is the unit ideal (`idxZero`).
4. The lemma `T.degree_images_eigenLines_cmUnitaryShimuraObject` gives
$$\deg_h N = \frac{p}{2}\operatorname{Re}\log\Omega(E,\chi) - \frac{\log\lvert N_{E/\mathbb{Q}}(\det g_P)\rvert}{2[E:\mathbb{Q}]},$$
and the same form for $\bar N$ with $0$ and $\det g_Q = 1$, so $\deg_h \bar N = 0$. This step uses $\chi$ and `IsHerm`.
5. The ranks. Since $\rho^2 = -d \neq 0$, $\rho \neq 0$, so $\bar\tau(\mathrm{rt}) = -\rho \neq \rho$. Then `CM.EigDec.eigen_decomposition` gives $\operatorname{rank} L = p$ and $\operatorname{rank} \bar L = 0$. The lemma `CM.Indep.letters_independent` says that the $p$ images are of rank 1 and independent, so $\operatorname{rank} N = p$ (`CMDiff.latRank_iSup`). Also $\operatorname{rank}\bar N = 0$.
6. For a full-rank sublattice, `T.lattice_degree_eq_sublattice_degree_add_log_index` gives
$$\deg_h L = \deg_h N + \frac{\log N(\mathrm{idx}(L, N))}{[K:\mathbb{Q}]},$$
and the same for $\bar L$, where the index term is $\log 1 = 0$.
7. Put $n = [K:\mathbb{Q}]/[E:\mathbb{Q}]$. By `T.absNorm_map_ringOfIntegers_hom'`, $N(\tau(\mathfrak n)\mathcal{O}_K) = N(\mathfrak n)^n$ and $N(\bar{\mathfrak n}) = N(\mathfrak n)$. So $N(\mathfrak n)^2 = \lvert N_{E/\mathbb{Q}}(\det g_P)\rvert$, and
$$\frac{\log N(\mathrm{idx}(L, N))}{[K:\mathbb{Q}]} = \frac{n \log N(\mathfrak n)}{n[E:\mathbb{Q}]} = \frac{\log\lvert N_{E/\mathbb{Q}}(\det g_P)\rvert}{2[E:\mathbb{Q}]}.$$
This term cancels the norm term of step 4, and a `linear_combination` closes the goal.

## In the Lean code

The theorem is at [CmObjectDefiniteLieEigenLatticeDegreeDifference.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CmObjectDefiniteLieEigenLatticeDegreeDifference.lean#L21). The helper `idxZero` is at line 11. Step 3 is at line 34, step 4 at line 43, step 6 at lines 91 and 92, and the final computation at lines 137 to 146.

- We have read the statements of the cited lemmas, not their proofs. We have not unfolded the statement `IndSt` of `letters_independent`; the facts in step 5 come from the fields that the proof extracts.
- Step 4 passes the global facts `cmCurve_closed`, `thetaUnifAV_all`, `abelianSchemeLaws_all.1` and `homExtension_semiAbelian_dvr_unconditional` to the degree lemma. So the real arithmetic input, the value $\operatorname{Re}\log\Omega(E,\chi)$, enters there.
- With $q = 0$ the lattice $\bar L$ has rank 0, and steps 4 and 6 show that its degree is 0. The theorem is in effect $\deg_h L = \tfrac{p}{2}\operatorname{Re}\log\Omega(E,\chi)$.
