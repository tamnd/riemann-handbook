---
title: The completely reducible case
decls:
  - GlobalTheory.ClassFin.cf_of_ss
  - GlobalTheory.T.classFiniteness_completelyReducible
  - GlobalTheory.T.finite_integral_classes_closedOrbit
  - GlobalTheory.ClassFin.finite_integral_classes_closed_orbit
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The completely reducible case

This section proves that a completely reducible rational group has finite class number over every adelic pair. The idea is due to Borel and Harish-Chandra. By the theorem of the last section, the group is the stabiliser of a rational tensor $t$ with a closed orbit. Class number one for $\mathrm{SL}_I$ turns a point of the group into a rational matrix $h$, and the tensor $t \cdot h$ has bounded denominators. Reduction theory for $\mathrm{SL}_I(\mathbb{R})$ shows that such tensors fall into finitely many classes under $\mathrm{SL}_I(\mathbb{Z})$. Each class gives one double coset. The result is the base case of the induction in the next section.

### Reduction theory

Fix a total order on $I$. For a complex tensor $v$ write $\|v\|^2 = \sum_k |v_k|^2$. A tensor $v$ is *minimal* if $\|v\| \leq \|w\|$ for every $w \in O(v)$.

**Definition 1.3.1 (Siegel set).** Let $C > 0$. A *Siegel triple* for $C$ is a triple $(k, a, n)$ of real matrices such that $k^{\mathsf{T}} k = 1$ and $\det k = 1$; $a$ is diagonal with entries $a_i > 0$, $\prod_i a_i = 1$ and $a_i \leq C a_j$ for $i < j$; and $n$ is lower triangular with $n_{ii} = 1$ and $|n_{ij}| \leq C$. The products $kan$ form the *Siegel set* $\mathfrak{S}_C \subseteq \mathrm{SL}_I(\mathbb{R})$.

This is the Iwasawa decomposition $\mathrm{SL}_I(\mathbb{R}) = K A N$ with $K = \mathrm{SO}_I(\mathbb{R})$, cut down to a region where the diagonal part does not decrease too fast and the unipotent part is bounded (see [Siegel sets](/learn/groups/#quotients-of-finite-volume)).

We use the following facts from the reduction theory of $\mathrm{SL}_I(\mathbb{R})$ and from the theory of minimal vectors. Let $d$ be a type.

1. If $O(v)$ is closed, then $O(v)$ contains a minimal tensor.
2. If $t$ is a real tensor and $O(t)$ contains a minimal tensor, then $t \cdot g$ is minimal for some $g \in \mathrm{SL}_I(\mathbb{R})$.
3. If $O(v)$ is closed, then for every $C$ there is $C'$ such that for every $y \in \mathrm{SL}_I(\mathbb{C})$ with $\|v \cdot y\|^2 \leq C$ there is $h \in \mathrm{SL}_I(\mathbb{C})$ with $v \cdot h = v$ and all entries of $hy$ bounded by $C'$ in absolute value.
4. If $v$ is minimal and $g \in \mathrm{SL}_I(\mathbb{C})$ fixes $v$, then the conjugate transpose $g^*$ fixes $v$.
5. There is $C$ such that for every $g \in \mathrm{SL}_I(\mathbb{R})$ there is $\gamma \in \mathrm{SL}_I(\mathbb{Z})$ with $g\gamma \in \mathfrak{S}_C$.
6. Let $v$ have the properties in the conclusions of 3 and 4. Then for all $C$ and $c > 0$ there is $B$ such that $\|v \cdot (kan)\|^2 \leq B$ for every Siegel triple $(k, a, n)$ for $C$ for which each entry of $v \cdot (kan)$ is $0$ or of absolute value at least $c$.

Fact 3 says that the orbit map $\mathrm{SL}_I(\mathbb{C})/\mathrm{Stab}(v) \to O(v)$ is proper. Fact 5 says that $\mathfrak{S}_C \, \mathrm{SL}_I(\mathbb{Z}) = \mathrm{SL}_I(\mathbb{R})$. Fact 6 is the core estimate of Borel and Harish-Chandra: on a Siegel set, a point of the orbit whose nonzero coordinates are bounded below has bounded norm. We do not prove these facts in this chapter.

**Lemma 1.3.2 (Finitely many integral classes in a closed orbit).** Let $t$ be a rational tensor of type $d$ with $O(t)$ closed, and let $D \geq 1$ be an integer. Then there is a finite set $Z$ of rational tensors of type $d$ such that for every $h \in \mathrm{SL}_I(\mathbb{Q})$ for which $D (t \cdot h)$ has integer entries there is $\gamma \in \mathrm{SL}_I(\mathbb{Z})$ with $t \cdot (h\gamma) \in Z$.

Lean: `GlobalTheory.T.finite_integral_classes_closedOrbit` (also `GlobalTheory.ClassFin.finite_integral_classes_closed_orbit`, a second name).

*Proof.* By facts 1 and 2 there is $g \in \mathrm{SL}_I(\mathbb{R})$ such that $v = t \cdot g$ is minimal. Then $O(v) = O(t)$, so $O(v)$ is closed, and $v$ has the conclusions of facts 3 and 4. Let $C$ be the constant of fact 5, and let $B$ be the constant of fact 6 for $v$, $C$ and $c = 1/D$. Let $Z$ be the set of rational tensors $w$ of type $d$ such that $Dw$ has integer entries and $\|w\|^2 \leq B$. It is finite: each entry of $w$ lies in $D^{-1}\mathbb{Z}$ and is bounded. Now let $h \in \mathrm{SL}_I(\mathbb{Q})$ with $D(t \cdot h)$ integral. Fact 5 applied to $g^{-1} h \in \mathrm{SL}_I(\mathbb{R})$ gives $\gamma \in \mathrm{SL}_I(\mathbb{Z})$ and a Siegel triple $(k, a, n)$ for $C$ with $g^{-1} h \gamma = kan$. Let $w = t \cdot (h\gamma)$. Then $Dw = (D (t \cdot h)) \cdot \gamma$ has integer entries, since $\gamma$ has integer entries. So each entry of $w$ is $0$ or of absolute value at least $1/D$. Also $v \cdot (kan) = t \cdot (g g^{-1} h \gamma) = w$. By fact 6, $\|w\|^2 \leq B$. So $w \in Z$. $\square$

### Class finiteness

**Theorem 1.3.3 (Class finiteness, completely reducible case).** Let $\Gamma \subseteq M_I(\mathbb{C})$ be a rational group that is completely reducible, and let $(R, R_0)$ be an adelic pair. Then $\Gamma$ has finite class number over $(R, R_0)$.

Lean: `GlobalTheory.ClassFin.cf_of_ss` (also `GlobalTheory.T.classFiniteness_completelyReducible`, a second name).

*Proof.* The [theorem on invariant tensors](/entry/exists-tensor-stabiliser-closed-orbit/) gives a rational tensor $t$ of type $d$ such that $\Gamma$ fixes $t$, every $y \in \mathrm{SL}_I(\mathbb{C})$ that fixes $t$ lies in $\Gamma$, and $O(t)$ is closed. Let $\Phi_k \in \mathbb{Q}[x]$ be the polynomials with $\Phi_k(y) = (t \cdot y)_k$ over every $\mathbb{Q}$-algebra.

*Step 1: every point fixes $t$.* For $g \in \Gamma$ we have $\Phi_k(g) = t_k$. So $\Phi_k - t_k \in \mathfrak{a}(\Gamma)$, and $t \cdot x = t$ for every $x \in \Gamma(R)$.

*Step 2: a rational representative with bounded denominators.* Let $D \geq 1$ be an integer such that $Dt$ has integer entries, and let $Z$ be the finite set of the last lemma for $t$ and $D$. Let $x \in \Gamma(R)$. Then $\det x = 1$ by the lemma on points of the first section, and the theorem on class number one for $\mathrm{SL}$ gives $x = hk$ with $h \in \mathrm{SL}_I(\mathbb{Q})$ and $k \in \mathrm{SL}_I(R)$ integral. By step 1, $t = t \cdot x = (t \cdot h) \cdot k$, so $t \cdot h = t \cdot k^{-1}$, where $k^{-1} = \operatorname{adj}(k)$ is integral. Each entry of $(Dt) \cdot k^{-1}$ is a sum of products of entries of $Dt$ and of $k^{-1}$, so it lies in $R_0$. So the entries of $D(t \cdot h)$ are rational numbers in $R_0$, hence integers. The lemma gives $\gamma \in \mathrm{SL}_I(\mathbb{Z})$ with $t \cdot (h\gamma) \in Z$. Now $x = (h\gamma)(\gamma^{-1} k)$, and $\gamma^{-1} k$ is integral with determinant $1$. So every $x \in \Gamma(R)$ is $x = h' k'$ with $h' \in \mathrm{SL}_I(\mathbb{Q})$, $k' \in \mathrm{SL}_I(R)$ integral, and $t \cdot h' \in Z$.

*Step 3: the finite set.* For each $z \in Z$ for which such a product $h'k' \in \Gamma(R)$ with $t \cdot h' = z$ exists, choose one, $h_z k_z$. Let $T$ be the set of these products $h_z k_z$. It is finite and lies in $\Gamma(R)$.

*Step 4: the decomposition.* Let $x = h'k'$ as in step 2, with $z = t \cdot h'$. Then
$$t \cdot (h' h_z^{-1}) = (t \cdot h') \cdot h_z^{-1} = (t \cdot h_z) \cdot h_z^{-1} = t,$$
and $\det(h' h_z^{-1}) = 1$. So $\gamma' = h' h_z^{-1}$ lies in $\Gamma$, and it is rational, so $\gamma' \in \Gamma(\mathbb{Q})$. Let $u = k_z^{-1} k'$. It is integral, since $k_z^{-1} = \operatorname{adj}(k_z)$ is. We have
$$x = h' k' = \gamma' \, (h_z k_z) \, u.$$
Finally $u = (h_z k_z)^{-1} \gamma'^{-1} x$ lies in $\Gamma(R)$, since $\Gamma(R)$ is closed under products and inverses and contains the image of $\Gamma(\mathbb{Q})$. $\square$

**Remark 1.3.4 (Formalization).** The six facts of reduction theory are, in order, `GlobalTheory.T.exists_minNormTensor_of_isClosed_tensorSLOrbit`, `GlobalTheory.T.exists_real_translate_isMinNormTensorInOrbit`, `GlobalTheory.T.tensorSLOrbit_map_proper_of_isClosed`, `GlobalTheory.T.minNormTensor_stabilizer_conjTranspose_invariant`, `GlobalTheory.T.exists_siegel_decomposition_mul_int_matrix_of_det_eq_one` and `GlobalTheory.T.nsq_act_le_of_isSiegel_of_entries_zero_or_ge`. They are proved in the same folder; we have opened their statements, not their proofs. Fact 6 has hypotheses 3 and 4 stated for the fixed tensor $v$, not the closedness of the orbit. The order on $I$ is chosen inside the proof of the lemma from an enumeration of $I$. The finiteness of $Z$ is `finite_bdd_denominator_vectors` in [FiniteIntegralClassesClosedOrbit.lean](lean:Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs/FiniteIntegralClassesClosedOrbit.lean#L43). The second name of the theorem is a wrapper proved by `first | exact ...` under `set_option maxHeartbeats 1000000`.
