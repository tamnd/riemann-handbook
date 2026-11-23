---
title: Splitting the Haar measure along a stabilizer
decls:
  - Formalism.L2.SG.Pf.NcS.SplitPf.omega_splitting_of_witt
  - Formalism.L2.SG.Pf.NcS.SplitPf.splitOm_of_intWitt
  - Formalism.L2.SG.Pf.NcReal.JX.realBracket_of_jac
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Splitting the Haar measure along a stabilizer

The normalizing constant of the theta lift compares two Haar measures: the measure on the unitary group $G$ of the big space and the measure on the stabilizer $H$ of a frame $X_0$. The comparison is a fibration $G \to G / H$, where $G/H$ is the orbit of $X_0$. This section proves two results of this kind. The first, the Theorem (Splitting the measure), splits the measure at the finite places and at infinity, with an explicit constant at the finite places given by local orbital volumes. The second, the Theorem (Real bracket), computes the constant at infinity. Both are used in the [Theorem 8.9.5](/entry/nc-tie0-all-of/) that ties the normalizing constant to the mass, and the second is used in the [Theorem 5.6](/entry/real-bracket-holds/) that proves the real bracket outright.

Let $E/F$ be a CM extension of number fields, $(V, h)$ a nondegenerate Hermitian space over $E$ of dimension $n$, and $G = \mathrm{U}(V, h)$ its [unitary group](/learn/groups/#unitary-groups). Let $X_0 = (x_1, \dots, x_m)$ be a family in $V$ with Gram matrix $\mathrm{Gram}(X_0) = (h(x_i, x_j))$ of nonzero determinant, and let $H \subseteq G$ be the subgroup of elements that fix each $x_i$. Let $\Lambda$ be a lattice in $V$, and for each finite place $v$ let $K_v$ be the stabilizer of $\Lambda_v$ in $G(F_v)$. Put $K_f = \prod_v K_v$.

**Definition 8.8.1 (Local orbital volume).** At a finite place $v$, the orbit of $X_0$ under $K_v$ is an open compact subset of the set of families $X$ in $V_v^m$ with $\mathrm{Gram}(X) = \mathrm{Gram}(X_0)$. The *local orbital volume* $\omega_v(\mathrm{Gram}(X_0), K_v X_0)$ is the measure of this orbit for the standard orbital measure on the set of families with Gram matrix $\mathrm{Gram}(X_0)$. We did not unfold the normalization of this measure.

**Definition 8.8.2 (Local Witt condition).** The *local Witt condition* holds if, at every finite place $v$, every family $X$ in $V_v^m$ with $\mathrm{Gram}(X) = \mathrm{Gram}(X_0)$ lies in the orbit $G(F_v) X_0$. The *integral Witt condition* holds if for almost all $v$ every such family $X$ in $\Lambda_v^m$ is $k X_0$ for some $k \in K_v$.

The local Witt condition is the theorem of Witt for Hermitian spaces over local fields: an isometry between subspaces of a nondegenerate Hermitian space extends to the whole space (O'Meara, *Introduction to Quadratic Forms*, §42, gives the quadratic case). The integral Witt condition is a statement about unimodular lattices at almost all places.

**Theorem 8.8.3 (Splitting the measure).** Assume the local and integral Witt conditions and the standing conditions: the standard hypotheses on the datum, $2(2r + 1) < n$, the admissibility of the measures, the compatibility of the stabilizer with the Siegel-Weil data, the standard normalization of the measures, the orbit condition and the compatibility condition, and $0 < \mu_{G_f}(K_f) < \infty$. Then there is $a' > 0$ such that:

1. for all admissible choices of the measures at infinity and of the fibre families, and all integrable $f$ on $G_\infty$,
$$\int_{G_\infty} f \, d\mu_{G_\infty} = a' \int_{y} \int_{H_\infty} f\bigl(s(y) h'\bigr) \, d\mu_{H_\infty}(h') \, dy,$$
where $s$ is a section of the fibration and $dy$ is the fibre measure;
2. at the finite places,
$$\mu_{G_f}(K_f) \, a' = \mu_{H_f}(K_f \cap H) \prod_v \omega_v\bigl(\mathrm{Gram}(X_0), K_v X_0\bigr).$$

Lean: `Formalism.L2.SG.Pf.NcS.SplitPf.omega_splitting_of_witt`.

*Proof.* Three inputs are combined. The first is that the tuple of measures is admissible. The second is the decomposition of the Haar measure of $G(F_v)$ along the orbit map $g \mapsto g X_0$ at each place $v$: the measure of $G$ is the product of the measure of $H$ and the orbital measure, by the local Witt condition, which makes the orbit map onto the set of families with Gram matrix $\mathrm{Gram}(X_0)$. The third is that the product of the local orbital volumes converges and is positive and finite, by the integral Witt condition: at almost all $v$ the orbit $K_v X_0$ is all of $\Lambda_v^m \cap \{\mathrm{Gram}(X) = \mathrm{Gram}(X_0)\}$. Then $a'$ is the ratio of the two global measures, and the finite part of this ratio is the product in part 2. $\square$

**Theorem 8.8.4 (Local Witt theorem).** The local Witt condition holds.

Lean: `Formalism.L2.SG.Pf.NcS.WittLocPf.local_witt_theorem`.

**Corollary 8.8.5 (Splitting the measure from the integral Witt condition).** Under the standing conditions of the Theorem (Splitting the measure) and the integral Witt condition, the conclusion of that theorem holds.

Lean: `Formalism.L2.SG.Pf.NcS.SplitPf.splitOm_of_intWitt`.

*Proof.* This is the [Theorem (Splitting the measure)](/entry/omega-splitting-of-witt/) applied to the Theorem (Local Witt theorem). $\square$

Now the constant at infinity. Let $h_\infty$ be the number of infinite places of $F$, $k$ the weight and $r$ the rank of the flag. Let $N$ and $N'$ be the unipotent radicals for the two words $u$ and $u'$, with fundamental domains $F_d N$ and $F_d N'$ of their integral points, and let $T_u$ be the norm parameter of $u$. Put
$$e(k, r) = -\frac{8 r^3 + 6 r^2 + 6 k r^2 + r}{3}.$$

**Definition 8.8.6 (Real bracket).** The *real bracket* holds if, for every Hida setting, all words $u, u'$, fundamental domains $F_d N, F_d N'$ in the standard setting, compatible measures, every standard character $\psi$, every $a' > 0$ and the archimedean clause for $a'$,
$$\begin{aligned} &D_C \cdot \mu_{H}(\mathrm{univ}) \, \mu_{N}(F_d N) \, \mu_{N'}(F_d N') \\ &\quad = a' \, 2^{k h_\infty} \Bigl(\frac{\pi^k}{(k-1)!}\Bigr)^{h_\infty} T_u^{-k h_\infty} \, |d_F|^{e(k, r)}, \end{aligned}$$
where $D_C$ is the constant of the datum.

The factor $|d_F|^{e(k,r)}$ comes from the covolumes of the unipotent lattices of the [previous section](/entry/block-covol-holds/), through the covolume reference below.

**Definition 8.8.7 (Covolume reference).** The *covolume reference* holds if, for every Hida setting and all $u, u'$ and fundamental domains in the standard setting, the product of the measures of $F_d N$ and $F_d N'$ under the reference measure of the block coordinates is $|d_F|^{e(k, r)}$.

**Theorem 8.8.8 (Real bracket).** Assume the Jacobian gauge identity, the covolume reference, the archimedean clause for $a'$, and the gauge density for every $n$ and every sign vector $\varepsilon \in \{\pm\}^n$. Then the real bracket holds.

Lean: `Formalism.L2.SG.Pf.NcReal.JX.realBracket_of_jac`.

*Proof.* The Jacobian gauge identity ([Theorem 5.8](/entry/jac-gauge-holds/)) and the covolume reference give the splitting of the measure at each infinite place: the measure of the unipotent domains is $|d_F|^{e(k,r)}$ times the product of the local Jacobian factors. The product of the local Jacobians over the infinite places is exact, by the product exactness theorem. The archimedean clause ([Theorem 5.7](/entry/aprime-inf-holds/)) gives the value $a'$ of the constant at infinity in terms of the local factor $2^k \pi^k / (k-1)!$ and $T_u^{-k}$ at each infinite place, and the gauge density fixes the normalization of $\mu_H$. Multiplying over the $h_\infty$ infinite places gives the formula. $\square$

**Remark 8.8.9 (Formalization).** The local and integral Witt conditions are defined twice with the same text, in NcSLocSB.lean (lines 19 and 27) and in NcXLocSB.lean (lines 19 and 27). The statement of the splitting also has two near copies ([NcSplitS.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/DualFamilyCounting/NcSplitS.lean#L13) and NcSplit.lean:15). Among the standing conditions, the one we call compatibility with the Siegel-Weil data has the name `StabilizerFirstChernCompatibility`, which suggests a statement about Chern classes; it is a condition on the measures. Another, `SWa1`, sits in a namespace named `UnusedSlot34`, but it is used. We did not unfold the archimedean clause, the gauge density or the measure compatibility conditions, so the proof of the Theorem (Real bracket) gives the role of each input as its name and statement show it. The covolume reference is stated for the reference measures of both words $u$ and $u'$ built from $u$ alone (NcRealXPS.lean:169).
