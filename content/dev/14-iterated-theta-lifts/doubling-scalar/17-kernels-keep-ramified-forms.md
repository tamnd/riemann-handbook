---
title: Kernels keep ramified forms
decls:
  - GlobalTheory.KRamT.kernel_keeps_ramT
  - GlobalTheory.T.chainStepKernel_preserves_levelRamifiedForms
  - GlobalTheory.AdForm.kernels_keep_ramL
  - GlobalTheory.T.chainKernel_preserves_ramifiedForms_liveCharts
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Kernels keep ramified forms

The see-saw laws of the last sections act on the ramified sets $R_j$ of functions on the groups of the spaces $X_j$. A ramified set must be stable under the kernel of each step of the chain, which maps functions at step $i$ to functions at step $i + 1$. This section proves this stability for the column chains of a twisted tower. The first theorem shows that the kernel maps forms that are ramified at the twist places to forms of the same kind. The second theorem adds the condition that the form vanishes at the charts that are not live. The result is used in [the column side](/entry/col-side-alt/) of the open orbit argument, for the multiplicity condition in branch 3 of the [unitary hypotheses](/proof/unitary-hypotheses/).

**Setting.** In this section we use the column chains of a twisted tower $I$, with laws $l$, a word $u$ and an index $a$. For each step $i$ of the chain there is a finite set $\mathrm{Cl}_i$ of *classes*. Each class $c$ has a representative point, a stabiliser $\mathrm{St}(c)$ and a weight $\mathrm{wt}_i(c)$. Let $\mathcal{V}_i$ be the space of vector valued functions of weight $\lambda_i$ on the frames of rank $N_i$, and let $\mathrm{tr}(c, g)$ be the translation by an element $g$ of the group of the class $c$. A *column form* at step $i$ is a function $\varphi$ on $\mathrm{Cl}_i$ with $\varphi(c)$ a function on the frames. Let $F_i$ be the space of column forms with $\varphi(c) \in \mathcal{V}_i$ and $\mathrm{tr}(c, g)\varphi(c) = \varphi(c)$ for all $c$ and all $g \in \mathrm{St}(c)$. For classes $c \in \mathrm{Cl}_i$ and $c' \in \mathrm{Cl}_{i+1}$ there is a linear *kernel entry* $\mathrm{km}_i(c, c')$, and the *kernel* of the step is
$$(\mathcal{K}_i \varphi)(c') = \sum_{c \in \mathrm{Cl}_i} \mathrm{wt}_i(c)\ \mathrm{km}_i(c, c')\big(\varphi(c)\big).$$
More generally, $\mathcal{K}_i$ is defined by the same formula on all functions on $\mathrm{Cl}_i$, and it is linear. The kernel entry is built from an unfolding map, which is the jet of the theta datum of the pair of representatives. The theta datum is built from the cell entry $\xi_i(c, c')$, a linear form on matrices.

At each twist place $p$ of the tower, with residue field $\mathbb{F}_p$, every unit $s \in \mathbb{F}_p^\times$ acts on classes by a *dilation* $c \mapsto \mathrm{dl}_i(p, s, c)$, and on functions by a transfer $\mathrm{dT}_i(p, s, c)$. The dilations form an action: $\mathrm{dl}_i(p, 1, c) = c$ and $\mathrm{dl}_i(p, s s', c) = \mathrm{dl}_i(p, s, \mathrm{dl}_i(p, s', c))$. They do not change the stabilisers.

**Definition 2.17.1 (Ramified column form).** A column form $\varphi$ at step $i$ is *ramified at the twist places* if $\varphi \in F_i$ and, for every twist place $p$ and every class $c$,
$$\sum_{s \in \mathbb{F}_p^\times} \mathrm{dT}_i(p, s, c)\Big(\varphi\big(\mathrm{dl}_i(p, s, c)\big)\Big) = 0.$$

So a ramified form has no part that is invariant under the dilations at a twist place.

**Theorem 2.17.2 (Kernels keep ramified forms).** Let $I$ be a valid twisted tower with laws $l$, let $i < m$, and let $\varphi$ be ramified at the twist places at step $i$. Then $\mathcal{K}_i \varphi$ is ramified at the twist places at step $i + 1$.

Lean: `GlobalTheory.KRamT.kernel_keeps_ramT` (also `GlobalTheory.T.chainStepKernel_preserves_levelRamifiedForms`, a second name).

*Proof.* We first show that $\mathcal{K}_i \varphi \in F_{i+1}$, and then that the kernel commutes with the dilation sums.

1. *Translation by one.* For every class, $\mathrm{tr}(c, 1)$ is the identity, since the unit acts trivially on the frames.
2. *The rational equivariance.* The theorem on the rational equivariance of kernel entries says the following. Let $f$ lie in the range of the sharp map on $\mathcal{V}_i$, and let $g, g'$ move the representatives of $c$ and $c'$. Then the kernel entry at the moved representatives, applied to the translate of $f$ by $g$, is the translate by $g'$ of the kernel entry applied to $f$. By the lemma on the sharp range, every $f \in \mathcal{V}_i$ lies in this range for $i < m$.
3. *Stabiliser invariance of an entry.* Let $f \in \mathcal{V}_i$ and $g \in \mathrm{St}(c')$. Apply step 2 with the unit at $c$ and with $g$ at $c'$. The unit fixes the representative of $c$, and $g$ fixes the representative of $c'$. By step 1, the identity becomes $\mathrm{tr}(c', g)\, \mathrm{km}_i(c, c')(f) = \mathrm{km}_i(c, c')(f)$.
4. *The kernel lies in $F_{i+1}$.* By the lemma on the values of kernel entries, $\mathrm{km}_i(c, c')$ maps $\mathcal{V}_i$ into $\mathcal{V}_{i+1}$. So $(\mathcal{K}_i \varphi)(c')$ is a finite sum of elements of $\mathcal{V}_{i+1}$. Each term is invariant under $\mathrm{St}(c')$ by step 3, and translation is linear, so the sum is invariant.
5. *Dilation of an entry.* Let $f \in \mathcal{V}_i$, $s \in \mathbb{F}_p^\times$ and write $\hat c = \mathrm{dl}_i(p, s, c)$, $\hat c' = \mathrm{dl}_{i+1}(p, s, c')$. We show
$$\mathrm{dT}_{i+1}(p, s, c')\big(\mathrm{km}_i(\hat c, \hat c')(f)\big) = \mathrm{km}_i(c, c')\big(\mathrm{dT}_i(p, s, c) f\big).$$
The dilated class is the class of the representative moved by a diagonal point, and the transfer is translation by that move. Step 2 with the two moves rewrites the left side as the entry at the moved representatives applied to the transfer of $f$. The entry does not change when both points change by the same diagonal unit. Indeed, the two characters of the pair and the theta datum are invariant under this change, by the lemmas on the diagonal characters and on the diagonal theta datum.
6. *Dilation of the kernel.* For fixed $p$ and $s$, the dilation $\mathrm{dl}_i(p, s, \cdot)$ is a bijection of $\mathrm{Cl}_i$, with inverse $\mathrm{dl}_i(p, s^{-1}, \cdot)$. The weight of a class depends only on its stabiliser, so $\mathrm{wt}_i(\mathrm{dl}_i(p, s, c)) = \mathrm{wt}_i(c)$. Reindex the sum that defines $\mathcal{K}_i \varphi$ at $\hat c'$ by this bijection. Then step 5 gives
$$\mathrm{dT}_{i+1}(p, s, c')\big((\mathcal{K}_i \varphi)(\hat c')\big) = \big(\mathcal{K}_i \varphi_s\big)(c'), \qquad \varphi_s(c) = \mathrm{dT}_i(p, s, c)\big(\varphi(\mathrm{dl}_i(p, s, c))\big).$$
7. *Conclusion.* Sum step 6 over $s$. Since $\mathcal{K}_i$ is linear, the sum is $\mathcal{K}_i$ applied to $\sum_s \varphi_s$. This function is zero, since $\varphi$ is ramified. So the dilation sum of $\mathcal{K}_i \varphi$ at $(p, c')$ is zero. With step 4, $\mathcal{K}_i \varphi$ is ramified at the twist places. $\square$

The theorem does not use the pins of the tower or the later data of the laws.

**Setting (Live charts).** A twist datum $A$ of the tower assigns to each class $c \in \mathrm{Cl}_j$ a chart $\mathrm{ch}_j(c)$ in an index set $\mathrm{Ch}^0_j$, and it carries cell entries $\xi_j(\alpha, \gamma, z)$ for charts $\alpha \in \mathrm{Ch}^0_j$ and $\gamma \in \mathrm{Ch}^0_{j+1}$. Let $\iota_j \colon \mathrm{Ch}_j \to \mathrm{Ch}^0_j$ be maps from smaller index sets. A chart is *live* if it is in the image of $\iota_j$, and *dead* otherwise. The maps $\iota$ are *live* for $A$ if each $\iota_j$ is injective, if $\iota_0$ and $\iota_m$ are surjective, and if $\xi_j(\alpha, \gamma, z) = 0$ for every dead $\gamma$, all $\alpha$ and all $z$. A column form $\varphi$ at step $j$ is *ramified on the live charts* if it is ramified at the twist places and $\varphi(c) = 0$ for every class $c$ whose chart is dead.

**Theorem 2.17.3 (Kernels keep ramified forms on live charts).** Let $I$ be a valid twisted tower with pins and laws $l$, let $A$ be a valid twist datum, and let the maps $\iota$ be live for $A$. Let $i < m$, and let $\varphi$ be ramified on the live charts at step $i$. Then $\mathcal{K}_i \varphi$ is ramified on the live charts at step $i + 1$.

Lean: `GlobalTheory.AdForm.kernels_keep_ramL` (also `GlobalTheory.T.chainKernel_preserves_ramifiedForms_liveCharts`, a second name).

*Proof.* By the last theorem, $\mathcal{K}_i \varphi$ is ramified at the twist places. Let $c' \in \mathrm{Cl}_{i+1}$ have a dead chart $\gamma = \mathrm{ch}_{i+1}(c')$. We show that $\mathrm{km}_i(c, c') = 0$ for every $c$, so that $(\mathcal{K}_i \varphi)(c') = 0$.

1. *The moved datum.* The theorem on the moved datum and the finite datum of a representative pair says the following. Let $\Phi$ be a function that is a standard half for the datum, and let $p$ be a number with $\Phi(z e) = p\, \xi_i(\alpha, \gamma, z)$ for all $z$. Then, for classes $c, c'$ with charts $\alpha, \gamma$, the value of $\Phi$ at the point $z e$ moved by the inverse moves of the pair is $p$ times the image of the cell entry $\xi_i(c, c')(z)$ under the complex embedding.
2. *The zero datum.* Take $\Phi = 0$ and $p = 1$. The zero function is a standard half. The hypothesis of step 1 holds, since $\gamma$ is dead and so $\xi_i(\alpha, \gamma, z) = 0$. The conclusion says that the image of $\xi_i(c, c')(z)$ is zero for every matrix $z$. The embedding is injective, and every linear map is given by a matrix, so $\xi_i(c, c') = 0$.
3. *The theta datum.* The theta datum of the pair is built from $\xi_i(c, c')$, and the theta datum of the zero entry is zero.
4. *The unfolding map.* The jet of the zero function is zero, since all its derivatives at the origin vanish. The linear map of a zero jet is zero, since it vanishes on the monomial basis. So the unfolding map of $(c, c')$ is zero.
5. *The kernel entry.* The kernel entry $\mathrm{km}_i(c, c')$ is a composite with the unfolding map, so it is zero. Hence every term of $(\mathcal{K}_i \varphi)(c')$ is zero. $\square$

The proof does not use that $\varphi$ vanishes at the dead charts of step $i$: the kernel vanishes at a dead chart for every input. Of the live condition, only the vanishing of $\xi$ at dead charts is used.

**Remark 2.17.4 (Formalization).** The first theorem is at [ChainStepKernelPreservesLevelRamifiedForms.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ChainStepKernelPreservesLevelRamifiedForms.lean#L132). In the same file, step 1 is at line 29, the diagonal invariance of step 5 at line 35, step 3 at line 42, step 4 at line 55, step 5 at line 80, and the bijection and reindexing of step 6 at lines 108 and 115. The second theorem is at [ChainKernelPreservesRamifiedFormsLiveCharts.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ChainKernelPreservesRamifiedFormsLiveCharts.lean#L12). The second names are restatements in [ChainStepKernelPreservesLevelRamifiedFormsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ChainStepKernelPreservesLevelRamifiedFormsStatement.lean#L13) and [ChainKernelPreservesRamifiedFormsLiveChartsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ChainKernelPreservesRamifiedFormsLiveChartsStatement.lean#L9). The ramified condition is defined in [LevChiEqOne.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/LevChiEqOne.lean#L84), the space $F_i$ in [PredMemGamRanks.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/PredMemGamRanks.lean#L151), and the live condition and the ramified condition on live charts in [PinColL.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/PinColL.lean#L17). In the formal first theorem, the pins and the later data are bound and not used. In the formal second theorem, the moved datum theorem is applied to the zero function only for its last clause. We have read the statements, not the proofs, of the rational equivariance of kernel entries, the sharp range, the values of kernel entries, the diagonal characters and theta datum, and the moved datum theorem. We have not unfolded the classes, the frames, the dilations and transfers, the sharp map, the theta datum and the jets; their descriptions above follow their names and the statements that use them.
