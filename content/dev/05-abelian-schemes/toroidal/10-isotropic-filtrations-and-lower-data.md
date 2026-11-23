---
title: Isotropic filtrations and lower data
decls:
  - GlobalTheory.LowDat.exists_lower
  - GlobalTheory.T.exists_isotropic_saturated_weight_filtration
  - GlobalTheory.LowFilt.exists_filt
  - GlobalTheory.T.exists_compatible_isometries_coisotropic_kernels
  - GlobalTheory.LowFilt.exists_compatible_isometries
  - GlobalTheory.T.lowerDatumObject_comes_from_base_of_linearPoints
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Isotropic filtrations and lower data

A degenerating family near a boundary point has a torus part of some rank $r$ and an abelian part. This section shows that the abelian part is an object of a smaller moduli problem, for a *lower* Hermitian datum $D'$ of signature $(p - r, q - r)$. The lattice $\Lambda$ of $D$ gets an isotropic saturated submodule $Z$ of rank $r$, and $D'$ is the quotient $Z^\perp / Z$. The submodule $Z$ comes from the level structures of the family. At each level $n$, the torsion points of the generic fibre have a lattice part, and the kernel of the lattice part is coisotropic modulo $n$. A tower of isometries of $\Lambda$ moves all these kernels to the one submodule $Z^\perp + n\Lambda$. This is the weight filtration of the boundary point, as in [toroidal and minimal compactifications](/learn/abelian-varieties/#toroidal-and-minimal-compactifications). We use the notation of Sections 1 and 2. $D$ is a Hermitian datum with lattice $\Lambda$, form $\langle \cdot, \cdot \rangle$ and signature $(p, q)$, and $l$ is a level with $M' = \operatorname{lcm}(M, A)$.

**Definition 7.10.1 (Isotropic saturated submodule, lower datum).** Let $Z \subseteq \Lambda$ be an $\mathcal{O}_E$-submodule.

1. The *orthogonal* of $Z$ is $Z^\perp = \{ x \in \Lambda : \langle x, z \rangle = 0 \text{ for all } z \in Z \}$. It is an $\mathcal{O}_E$-submodule, because $\langle a x, z \rangle = \langle x, \bar a z \rangle$.
2. $Z$ is *isotropic saturated* if $Z \subseteq Z^\perp$, and $n x \in Z$ with $n \ne 0$ an integer implies $x \in Z$.
3. Let $D'$ be a Hermitian datum with lattice $\Lambda'$. An $\mathcal{O}_E$-linear map $f : Z^\perp \to \Lambda'$ makes $D'$ a *lower datum* of $D$ for $Z$ if $f$ is surjective, $f(x) = 0$ exactly when $x \in Z$, and $\langle f x, f y \rangle' = \langle x, y \rangle$ for all $x, y \in Z^\perp$.
4. The *lower level* $l'$ of $l$ is the level with the same $M$ and $\mathfrak{M}$, and with $A$ replaced by $M'$.

Lean: `GlobalTheory.LowDat.IsIsoSat` (also `GlobalTheory.LowDat.perp`, `GlobalTheory.LowDat.IsLower`, `GlobalTheory.LowDat.lowLevel`).

For the lower level, $\operatorname{lcm}(M, M') = M'$, so $l'$ has the same $M'$ as $l$, and $K_{M'} \subseteq F$ for each coefficient field $F$ of $l$.

**Definition 7.10.2 (Coisotropic map, kernel shape).** Let $X$ be an $\mathcal{O}_E$-module, $y : \Lambda \to X$ an $\mathcal{O}_E$-linear map, $n \ge 1$ and $Z \subseteq \Lambda$ a submodule.

1. $y$ is *coisotropic modulo $n$* if $y$ is surjective modulo $nX$, and if each $a \in \Lambda$ with $n \mid \langle a, b \rangle$ for all $b$ with $y(b) \in nX$ has $y(a) \in nX$.
2. The kernel of $y$ *has the shape $Z$ modulo $n$* if, for all $a \in \Lambda$, $y(a) \in nX$ exactly when $a \in Z^\perp + n\Lambda$.
3. Two submodules $Z, Z'$ form an *opposite pair* if both are isotropic, and the form identifies each with the $\mathbb{Z}$-dual of the other.

Lean: `GlobalTheory.LowFilt.Cois` (also `GlobalTheory.LowFilt.KerIs`, `GlobalTheory.LowFilt.IsOpp`).

**Theorem 7.10.3 (Compatible isometries).** Let $X$ be an $\mathcal{O}_E$-module that is free of finite rank over $\mathbb{Z}$, with $\operatorname{rank}_{\mathcal{O}_E} X \le \min(p, q)$. Let $y_n : \Lambda \to X$ for $n \in \mathbb{N}$ be $\mathcal{O}_E$-linear maps such that $y_n$ is coisotropic modulo $n$ for $n > 0$, and such that $y_{nm}(a) \equiv y_n(a) \pmod{nX}$ for $n, m > 0$. Let $N > 0$. Then there are an isotropic saturated $Z \subseteq \Lambda$ with $\operatorname{rank}_{\mathcal{O}_E} Z = \operatorname{rank}_{\mathcal{O}_E} X$ and isometries $g_n$ of $(\Lambda, \langle \cdot, \cdot \rangle)$ with:

1. $g_{nm}(a) \equiv g_n(a) \pmod{n\Lambda}$ for $n, m > 0$;
2. $g_n(a) \equiv a \pmod{N\Lambda}$ for all $n$;
3. for $n > 0$, the kernel of $y_n \circ g_n$ has the shape $Z$ modulo $n$.

Lean: `GlobalTheory.LowFilt.exists_compatible_isometries` (also `GlobalTheory.T.exists_compatible_isometries_coisotropic_kernels`, a second name).

*Proof.* Let $r = \operatorname{rank} X$.

1. As $r \le \min(p, q)$, there is an isotropic saturated $Z_0$ of rank $r$, and it has an opposite $Z_0'$. A lemma on transversals gives an opposite $Z_1'$ of $Z_0$ that fits $y_N$. A lemma on coisotropic kernels then gives an isometry $g_0$ such that the kernel of $y_N \circ g_0$ has the shape $Z_0$ modulo $N$, up to the transform by $g_0$. Put $Z = g_0(Z_0)$. It is isotropic saturated of rank $r$, it has an opposite, and the kernel of $y_N$ has the shape $Z$ modulo $N$.
2. Put $n_j = N (j + 1)!$. A step lemma says: if the kernel of $y_{n_{j+1}} \circ G$ has the shape $Z$ modulo $n_j$, there is an isometry $h \equiv \mathrm{id} \pmod{n_j}$ such that the kernel of $y_{n_{j+1}} \circ G \circ h$ has the shape $Z$ modulo $n_{j+1}$. The tower relation of the $y_n$ moves the shape from $y_{n_j}$ to $y_{n_{j+1}}$ modulo $n_j$. By induction this gives isometries $S_j$ with $S_0 = \mathrm{id}$, $S_{j+1} \equiv S_j \pmod{n_j}$, and the kernel of $y_{n_j} \circ S_j$ of the shape $Z$ modulo $n_j$.
3. Put $g_n = S_n$. Since $n \mid n_n$, and the shape modulo a multiple gives the shape modulo $n$ for a map that is surjective modulo $n$, the kernel of $y_n \circ g_n$ has the shape $Z$ modulo $n$. The congruences of the $S_j$ give properties 1 and 2. $\square$

**Definition 7.10.4 (Level isometry, graded filtration).** Let $R$ be a local domain that is a Mumford base, and let $(t, P, y)$ be a family over $R$ as in the definition of a monomial family, with no $s_i$ and $\delta_i$. Let $F'$ be a field over $\operatorname{Frac} R$.

1. A *level isometry* $I$ over $F'$ is a root of unity $\zeta$ and, for each $n > 0$, a surjective $\mathcal{O}_E$-linear map $I_n$ from $\Lambda$ onto the $n$-torsion points of the generic fibre of $t$ over $F'$, with kernel $n\Lambda$, compatible in towers, that takes $\langle \cdot, \cdot \rangle$ to the Weil pairing. Through the uniformization $P$ each $n$-torsion point $Q$ has a *lattice part* $Q_y$ in $X_P / n X_P$.
2. $I$ *matches the level of $X_F$* if $\zeta_{M'}$ is the root of unity of $F$, and if the points $I_A(a)$ and $I_M(a)$ correspond to the level structure of the universal datum at $y$.
3. $I$ is *graded by $Z$* if for each $n > 0$ and $a \in \Lambda$, the point $I_n(a)$ has lattice part $0$ exactly when $a \in Z^\perp + n\Lambda$.

Lean: `GlobalTheory.LowDat.FiltGraded` (also `GlobalTheory.LowDat.XFLevel`, `GlobalTheory.LowDat.LowGraded`).

The lattice part of $I_n$ is a map $y_n : \Lambda \to X_P$ modulo $n$. A grading by $Z$ says that the kernel of $y_n$ has the shape $Z$ modulo $n$. A *lower grading* by a lower datum $D'$ adds level isometries $I'$ of the lower object, at the lower level, such that $I_n(a)$ for $a \in Z^\perp$ has lattice part $0$ and abelian part $I'_n(f a)$.

**Theorem 7.10.5 (Isotropic weight filtration).** Let $R$ be a local domain that is a Mumford base and $(t, P, y)$ a family over $R$ with $\operatorname{rank}_{\mathcal{O}_E} X_P \ge 1$. Then there are an isotropic saturated $Z \subseteq \Lambda$ with $\operatorname{rank} Z = \operatorname{rank} X_P$, and a datum $t_K$ on $\operatorname{Spec} \operatorname{Frac} R$ with maps to $t$ and to the universal datum at $y$, such that for each algebraically closed field $F'$ over $\operatorname{Frac} R$ there is a level isometry over $F'$ that matches the level of $X_F$ and is graded by $Z$.

Lean: `GlobalTheory.LowFilt.exists_filt` (also `GlobalTheory.T.exists_isotropic_saturated_weight_filtration`, a second name).

*Proof.* The family gives $t_K$ and its two maps. Let $F_0$ be an algebraic closure of $\operatorname{Frac} R$. The torsion of $t$ has the uniformized form at each level. A lemma gives a level isometry $I_0$ over $F_0$ that matches the level of $X_F$. A second lemma says that the lattice parts $y_n$ of $I_0$ are coisotropic modulo $n$. The tower property of $I_0$ gives $y_{nm}(a) \equiv y_n(a) \pmod{n}$. The rank of $X_P$ is at most $\min(p, q)$ for such a family. The theorem on compatible isometries with $N = M'$ gives $Z$ and isometries $g_n$. Let $I_1$ be the twist $I_{1,n}(a) = I_{0,n}(g_n a)$. It is again a level isometry. It matches the level of $X_F$, because the level points come from $I_{0,k}$ with $k \mid M'$ and $g_k(a) \equiv a \pmod{M'}$. A lemma extends $I_1$ to $F'$ with the same lattice parts. By property 3 of the isometries, the lattice part of $I_{1,n}(a)$ is $0$ exactly when $a \in Z^\perp + n\Lambda$. $\square$

**Theorem 7.10.6 (Lower datum of a family).** Let $R$ and $(t, P, y)$ be as in the previous theorem, and $r = \operatorname{rank}_{\mathcal{O}_E} X_P$. Then there are:

1. an isotropic saturated $Z \subseteq \Lambda$ of rank $r$;
2. a lower datum $D'$ of $D$ for $Z$, with $f : Z^\perp \to \Lambda'$, of signature $(p - r, q - r)$;
3. an object $o'$ of the moduli problem of $D'$ and $l'$ over $\operatorname{Spec} R$, and an isomorphism $\varphi_B$ from the group of $o'$ to the abelian part of $P$ that respects the action of $\mathcal{O}_E$ and takes the line bundle of $P$ to that of $o'$ by a generating isomorphism;
4. a datum $t_K$ on $\operatorname{Spec} \operatorname{Frac} R$ as before, such that over each algebraically closed $F'$ there are level isometries $I$ for $t$ and $I'$ for $o'$, where $I$ matches the level of $X_F$, $I$ is graded by $Z$, and $I$ has the lower grading by $D'$ with $I'$ and $\varphi_B$.

Lean: `GlobalTheory.LowDat.exists_lower`.

*Proof.* The theorem on the isotropic weight filtration gives $Z$. A lemma on lower data of isotropic saturated submodules gives $D'$, $f$ and the signature. A lemma on the abelian part, with Tate isometries, gives $o'$, $\varphi_B$ and the lower grading. $\square$

**Definition 7.10.7 (Lower base).** Let $D'$ be a Hermitian datum and $F$ a coefficient field for $l$. A *lower base* $L$ for $D'$ consists of a regular local domain $W$ with a map $b : F \to W$ of essentially finite type, an object $o$ of the moduli problem of $D'$ and $l'$ over $\operatorname{Spec} W$, degeneration data $Q$ over $W$ with character lattice $X_Q$ and an action of $\mathcal{O}_E$, and an isomorphism $\varphi_B$ from the group of $o$ to the abelian part of $Q$ as in item 3 above. In addition, $L$ satisfies two *fineness* conditions: two maps $W \to A$ to a reduced ring, or to the dual numbers, that agree on $F$ and carry the points $c(y)$ of $Q$ to the same points of one object $o''$, are equal. Finally, $\dim W + \operatorname{trdeg}_F \kappa(W) = n_{D'} + \operatorname{rank}(X_Q)\, \tfrac{[E:\mathbb{Q}]}{2}(p' + q')$.

Lean: `GlobalTheory.UCanon.LowBase` (also `GlobalTheory.UCanon.LowObj`).

**Theorem 7.10.8 (Lower base of linear points).** Let $V$ be a local domain with a map $b_V : F \to V$, $o'$ an object of the moduli problem of $D'$ and $l'$ over $\operatorname{Spec} V$, and $X$ an $\mathcal{O}_E$-module, free of finite rank over $\mathbb{Z}$. Let $x : X \to G_{o'}(V)$ be additive and $\mathcal{O}_E$-linear. Then there are a lower base $L$ for $D'$, a local map $\theta_0 : W \to V$ with $\theta_0 \circ b = b_V$, an isomorphism $e : X \to X_Q$ and a map of objects $m : o' \to o$ over $\operatorname{Spec} \theta_0$, such that $\varphi_B \circ m \circ x(y) = c(e y) \circ \operatorname{Spec} \theta_0$ for each $y \in X$.

Lean: `GlobalTheory.T.lowerDatumObject_comes_from_base_of_linearPoints`.

*Proof.* This is [the theorem on lower bases of linear points](/entry/low-base-of-linear-points/) applied to $V$, $o'$, $X$ and $x$. $\square$

**Remark 7.10.9 (Formalization).** The proofs are in [ExistsCompatibleIsometriesCoisotropicKernels.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsCompatibleIsometriesCoisotropicKernels.lean#L87), [ExistsIsotropicSaturatedWeightFiltration.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsIsotropicSaturatedWeightFiltration.lean#L54) and [ImportsTailExtra.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ImportsTailExtra.lean#L15). The module name `ImportsTailExtra` does not describe `exists_lower`. The `T.*` names are wrappers that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. `T.lowerDatumObject_comes_from_base_of_linearPoints` wraps `UCanon.lowBase_of_linearPoints` of [LowerDatumObjectComesFromBaseOfLinearPoints.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/LowerDatumObjectComesFromBaseOfLinearPoints.lean#L15), whose entry is in a later section. `perp`, `IsIsoSat`, `IsLower`, `lowLevel`, `XFLevel`, `FiltGraded` and `LowGraded` are in [FiltGraded.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FiltGraded.lean#L16), and `IsOpp`, `Cois` and `KerIs` in [CmHostUnitAddConjEqOne.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CmHostUnitAddConjEqOne.lean#L16); that module name does not describe them either. `LowBase` and `LowObj` are in [HasRigidCoords.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HasRigidCoords.lean#L29). The family $(t, P, y)$ is a `UChart.Fam`, with no invariant function; the bound $\operatorname{rank} X_P \le \min(p, q)$ comes from `T.finrank_uChart_le_min_signature`. In `exists_compatible_isometries` the isometry $g_n$ is `S n`, built at the level $N(n+1)!$, which is a multiple of $n$ (line 177); the induction is along `levelSeq N j` $= N (j+1)!$ at line 67 with `exists_step` at line 58. The twist of a level isometry is `twistI` at line 28 of the second file. The proofs apply `T.exists_isotropicSaturatedSubmodule_of_finrank_le`, `T.exists_oppositeIsotropicPair`, `T.exists_opposite_transversal_isotropic`, `T.exists_isometry_kernel_coisotropic_mod`, `FlatTors.torsionIso_holds`, `T.exists_levelIsometry_genericFibre_boundaryChart`, `T.tateIso_latticePart_surjective_coisotropicKernel`, `T.exists_levelIsometry_extension_algClosed`, `T.exists_equiv_latticePart_zero_iff_mem_nsmul`, `T.exists_lower_datum_of_isotropic_saturated` and `T.exists_lowerObject_abelianPart_tateIsometry`. They have no entries in this chapter, and we use only their statements. In the signature, $p - r$ and $q - r$ are differences of natural numbers, truncated at $0$. We have not unfolded `Obj`, `TateIsoQ`, `TateIso`, `QkPt`, `DegPre`, `IsGrpPullback`, `PELUnif` or the fields `fineRed`, `fineEps` and `dim` of `LowBase` beyond the summary above.
