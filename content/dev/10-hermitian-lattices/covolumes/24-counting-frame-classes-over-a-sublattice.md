---
title: Counting frame classes over a sublattice
decls:
  - GlobalTheory.LoopC.FixedLift.card_frames_le
  - GlobalTheory.T.card_integral_frames_fixed_lift_le
  - GlobalTheory.LoopC.FrEx.cntCl_ExSet_le
  - GlobalTheory.T.card_exactGramIntegralFrameClasses_le
  - GlobalTheory.LoopC.FrCount.main
  - GlobalTheory.T.frameTermCount_sublattice_bound
  - GlobalTheory.LoopC.TermsOver.main
  - GlobalTheory.T.count_terms_gramClass_over_sublattice
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Counting frame classes over a sublattice

The terms of the double coset sum over one row lattice are grouped by the Gram class of their frames and by a sublattice that the term sees in the anisotropic part. This section bounds the number of classes of terms in one group by a power of a height. The bound is proved in four steps, from the most rigid count to the one that the proof uses: frames with a fixed lift, frames with an exact Gram matrix, frames whose Gram matrix lies in a class, and terms whose Gram class has bounded height. The last count feeds [the step](/step/nonempty-hyps/).

We work in the global setting of the double coset sum. The field $E$ is a CM field of degree $2f$ with root discriminant $r_E$. The Hermitian space $V$ has a decomposition
$$V = X \oplus W_b \oplus Y,$$
with $X$ and $Y$ isotropic of rank $r_S$ and in duality, and an embedding $\iota$ of a $k$-dimensional Hermitian space $W$ into $V$. A row lattice $\Lambda$ for the base flag $F_0$ has a lattice $L_0(\Lambda)$ in $W$. The integer $T_u$ is the parameter of the word $u$, and $\mathfrak{d}$ is the fixed ideal of the setting, with $\mathrm{N}(\mathfrak{d}) = r_E^{2f}$.

**Definition 2.24.1 (Equivalence classes).** Let $X$ be a set with a relation $R$. The *number of classes* of $(X, R)$ is the number of distinct sets $\{ b \in X : R(a, b) \}$ with $a \in X$. When $R$ is an equivalence relation, this is the number of equivalence classes.

**Definition 2.24.2 (Admissible sublattice).** Let $L \subseteq W$ be a lattice, $1 \le s \le k$ and $Q \ge 1$. A sublattice $P \subseteq L$ is *admissible* for $(L, s, Q)$ if $P$ has rank $k - s$, if the index of $P$ in its saturation $\operatorname{sat}_L(P) = L \cap (E \otimes P)$ is at most $Q$, and if the determinant of the Gram matrix of $P$ is at most $Q$.

**Definition 2.24.3 (Sets of frames).** Let $\Lambda$ be a row lattice for $F_0$, $Z$ an $(r_S+1) \times (r_S+1)$ matrix and $P \subseteq W$ a sublattice. Let $\hat Z(F_0, F')$ be the Gram matrix of the frames, as in [Section 2.23.5](/entry/covolume-integral-unipotent-stabilizer-of-term/).

1. The *frame set* $\mathcal{F}(Z, P)$ is the set of terminal flags $F'$ for $\Lambda$ and $F_0$ with $\hat Z(F_0, F')$ equivalent to $Z$ under unitriangular changes, such that $P$ lies in the lattice that the term of $(F_0, F')$ sees in $W$. Two flags in it are related if they differ by an integral unipotent isometry of $F_0$ and an equivalence of frames.
2. The *exact set* $\mathcal{E}(Z, P)$ is the set of lifts $F'$ for $\Lambda$ whose vectors $e'_a$ lie in $\Lambda$, with $\hat Z(F_0, F') = Z$ exactly and with $P$ seen as above.
3. Given a map $\varphi : P \to V$, the *fixed set* $\mathcal{X}(Z, P, \varphi)$ is the set of lifts $F'$ for $\Lambda$ with $e'_a \in \Lambda$, with $\hat Z(F_0, F') = Z$, and with $h(\iota p + \varphi(p), f'_b) = 0$ for all $p \in P$ and all $b$.

The lattice $\Lambda$ is *split* if it is the sum of the standard lattice of $X$, of $\Lambda \cap W_b$, and of the standard lattice of $Y$ spanned by the $x\, e^*_a$ with $x \in \mathfrak{d}^{r_S - a}$.

**Definition 2.24.4 (Gram bounds).** For a Gram matrix $Z$ let $D_l(Z)$ be its leading minors, let
$$G(Z) = D_{r_S+1}(Z) \overline{D_{r_S+1}(Z)} - T_u T_{u'}\, D_{r_S}(Z) \overline{D_{r_S}(Z)},$$
and for a column $b_0$ let $M_{b_0}(Z)$ be the minor of the first $r_S$ rows with column $b_0$ removed. A number $Q$ *bounds* $Z$ if $Q \ge 1$, $r_E^{2f r_S} \le Q$, some $M_{b_0}(Z) \ne 0$ has $\prod_\tau |\tau M_{b_0}(Z)|^2 \le Q$, $G(Z) \ne 0$ and $\prod_\tau |\tau G(Z)| \le Q$. Put
$$\begin{aligned} \beta_{\mathrm{fix}}(s, N, D_e, Q) &= 9^{sf} (D_e^2 N^2 Q)^{s + s r_S} Q^{2 r_S^2}, \\ \beta_{\mathrm{fr}}(s, N, D_e, Q) &= N^{2 r_S} D_e^{r_S}\, \beta_{\mathrm{fix}}(s, N, D_e, Q). \end{aligned}$$

In all statements below we assume the standing hypotheses of the setting, that $F_0$ is the base flag of $u$, that $\Lambda$ is a row lattice for $F_0$, that $P$ is admissible for $(L_0(\Lambda), s, D_e)$, that $Q$ bounds $Z$, and we write $N = T_u^f$.

**Lemma 2.24.5 (Frames with a fixed lift).** Assume in addition that $\Lambda$ is split, and let $\varphi : P \to V$ be $\mathcal{O}_E$-linear with values in the standard lattice of $X$. Then the number of classes of $\mathcal{X}(Z, P, \varphi)$ is at most $\beta_{\mathrm{fix}}(s, N, D_e, Q)$.

Lean: `GlobalTheory.T.card_integral_frames_fixed_lift_le` (also `GlobalTheory.LoopC.FixedLift.card_frames_le`, its proof).

*Proof.* The data give a nonzero ideal $I$ of controlled norm such that the vectors of $W$ orthogonal to $P$ in the integral lattice form a lattice $S_0$ of rank $s$ with the right congruence properties; its norm is bounded through the admissibility of $P$ and $\mathrm{N}(\mathfrak{d}) = r_E^{2f}$. Take $F' \in \mathcal{X}(Z, P, \varphi)$. Since $h(\iota p + \varphi(p), f'_b) = 0$ for $p \in P$, the components of the frame vectors $f'_b$ in $W$ are vectors $w_b$ orthogonal to $P$, and they lie in $S_0$. Cover the tuples $(w_b)$ by a finite set of tuples $w^0$ modulo $I$; the number of residues is bounded by $9^{sf}$ times a power of $D_e^2 N^2 Q$ with exponent $s(1 + r_S)$. An Eichler transformation, which is an integral unipotent isometry fixing the frame of $F_0$, moves $F'$ so that its $W$-components equal the chosen $w^0$. Two frames in $\mathcal{X}$ with the same Gram matrix and the same $W$-components differ by a solution of a skew-Hermitian linear system on their $X$-components. These $X$-components are counted modulo $\mathfrak{d}^{r_S}$ through a nonzero row minor of $Z$, whose norm is at most $Q$; this gives at most $Q^{2 r_S^2}$ classes. Last, a central element of the integral unipotent group that fixes the frame of $F_0$ moves one solution to another in the same class. Multiplying the two counts gives the bound. $\square$

**Lemma 2.24.6 (Frames with an exact Gram matrix).** Assume that $\Lambda$ is split. Then the number of classes of $\mathcal{E}(Z, P)$ is at most $\beta_{\mathrm{fix}}(s, N, D_e, Q)$.

Lean: `GlobalTheory.T.card_exactGramIntegralFrameClasses_le` (also `GlobalTheory.LoopC.FrEx.cntCl_ExSet_le`, its proof).

*Proof.* For each $F' \in \mathcal{E}(Z, P)$ the sublattice $P$ lifts into $V$ along $F'$: there is $\varphi : P \to V$ with values in the standard lattice of $X$ such that $F'$ lies in $\mathcal{X}(Z, P, \varphi)$. Two lifts of $P$ differ by a unipotent isometry that fixes the frame of $F_0$ and preserves $\Lambda$, so after a move inside the class one lift $\varphi$ serves for all of $\mathcal{E}(Z, P)$. The count is then the count of the last Lemma. $\square$

**Proposition 2.24.7 (Frame classes over a sublattice).** The number of classes of $\mathcal{F}(Z, P)$ is at most $\beta_{\mathrm{fr}}(s, N, D_e, Q)$.

Lean: `GlobalTheory.T.frameTermCount_sublattice_bound` (also `GlobalTheory.LoopC.FrCount.main`, its proof).

*Proof.* First reduce to an exact Gram matrix. Every class of $\mathcal{F}(Z, P)$ contains a frame $F'$ with $\hat Z(F_0, F')$ in a fixed finite set of exact matrices: a unitriangular change brings the Gram matrix to $Z$, up to the choice of the change modulo the integral ones. The factor $N^{2r_S} D_e^{r_S}$ of $\beta_{\mathrm{fr}}$ bounds the number of exact matrices that occur. Next reduce to a split lattice. There is an isometry that fixes the frame of $F_0$ and maps $\Lambda$ to a split row lattice; it maps the frame sets bijectively and respects the relation. Then apply the last Lemma to each exact matrix. A map from the classes of $\mathcal{F}$ to the union of the classes of the exact sets, which is injective on classes, gives the bound. $\square$

**Theorem 2.24.8 (Terms over a Gram class).** For all constants of the setting there is $C_0$ such that for every $C \ge C_0$ the following holds. Let $Z$ be a Gram matrix in a relevant cell, that is, $\hat Z^{\pm}$ lies in the Bruhat cell of some point $p$. Let $1 \le s \le k$, let $P \subseteq L_0(\Lambda)$ be a sublattice of rank $k - s$, and let $D_e \ge 1$ with $\det P \le D_e$. Let $H_h$ satisfy $\mathrm{H}(b, C, Z) \le H_h$ and $D_e \le H_h^3$. Then the number of classes of $\mathcal{F}(Z, P)$ is at most
$$N^{2 r_S}\, D_e^{r_S}\, 9^{sf}\, H_h^{9s + 9s r_S + 16 r_S^2}.$$

Lean: `GlobalTheory.T.count_terms_gramClass_over_sublattice` (also `GlobalTheory.LoopC.TermsOver.main`, its proof).

*Proof.* If $\mathcal{F}(Z, P)$ is empty there is nothing to prove. Otherwise pick $F'$ in it. There is a matrix $Z_1$ equivalent to $Z$ such that $Q = \mathrm{H}(b, C, Z)^2$ bounds $Z_1$; this uses the choice of $C_0$ and the standing hypotheses. The sets of frames for $Z$ and for $Z_1$ coincide, since they depend only on the equivalence class. The sublattice $P$ is admissible for $(L_0(\Lambda), s, D_e)$: its determinant is at most $D_e$, and the square of the index of $P$ in its saturation divides the order of the discriminant module of $P$, which is the determinant of the definite lattice $P$. Apply [Proposition 2.24.7](/entry/frame-term-count-sublattice-bound/) with $Z_1$, $D_e$ and $Q$. With $N = T_u^f$ we have $N^2 \le \mathrm{H}(b, C, Z) \le H_h$ by the standing bound on $T_u$, and $Q \le H_h^2$. Then
$$\begin{aligned} \beta_{\mathrm{fr}}(s, N, D_e, Q) &\le N^{2r_S} D_e^{r_S} 9^{sf} (H_h^{6} H_h H_h^{2})^{s + s r_S} H_h^{4 r_S^2} \\ &\le N^{2r_S} D_e^{r_S} 9^{sf} H_h^{9s + 9s r_S + 16 r_S^2}. \end{aligned}$$
$\square$

**Remark 2.24.9 (Formalization).** The number of classes `cntCl` ([CntPartners.lean](lean:Formalism/SharpRestriction/CuspSpanNormBounds/CntPartners.lean#L172)) counts the distinct sets $\{b : R(a, b)\}$; it is the number of classes only when the relation is an equivalence relation, and the relation `TEqv` (line 177) is not proved to be one here. When $\mathcal{F}(Z, P)$ is empty, `TermsOver.main` ([CountTermsGramClassOverSublattice.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/CountTermsGramClassOverSublattice.lean#L228)) holds trivially. The steps of its proof are `exists_gram_representative_size_le_HH_sq`, `subOK_of` (line 156, through `definiteLattice_discriminantModule_card_det_sq`), `frB_le` (line 193) and `NT_sq_le` (line 118). The reduction to a split lattice is `exists_frameFixing_isometry_split_rowLattice`, the exact Gram representative is `exists_exactGram_frame_in_termClass`, and the lifts are `exists_sublattice_lifts_modulo_fixing_unipotent`. The fixed-lift count ([CardIntegralFramesFixedLiftLe.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/CardIntegralFramesFixedLiftLe.lean#L412)) uses `frames_same_gram_differ_by_skew_solution`, `fixed_frames_perpendicular_vectors`, `perpendicular_rank_ideal_bound` and the Eichler maps `eich` (line 390) and `eich_single` (line 344), with $\mathrm{N}(\mathfrak{d}) = r_E^{2f}$ as `ddI_norm` (line 250). These lemmas are cited by name and not unfolded here, so the account of the exponents in the proofs above follows the shape of the bounds. The sets of frames are `FrSet`, `ExSet` and `FixSet` in [RowMinor.lean](lean:Development/AbelianVarietyTheory/Definitions/SemilocalFrames/RowMinor.lean#L61); the seen lattice `seen` is not unfolded.
