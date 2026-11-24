---
title: Folding and multiplicity
decls:
  - Formalism.L2.SG.Pf.foldOKC_holds_of
  - Formalism.L2.SG.Pf.multPoly_holds_of'
  - Formalism.L2.SG.Pf.multPoly_holds_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Folding and multiplicity

The Poincaré series of the global argument is a sum over the rational points of a Bessel subgroup. To fold it into an integral over a fundamental domain, the proof needs that a compact set meets only a bounded number of translates of a rational point, and that the bound grows at most polynomially at the infinite places. This section proves the polynomial bound on the multiplicity from the [lattice count](/entry/lattice-count-all/), and then assembles the [folding](/entry/fold-okc-holds/) of the Poincaré series from it. The folding is used in the [nonempty hypotheses](/step/nonempty-hyps/), where the global data are shown to exist. We keep the setting of [adelic unitary groups](/entry/adelic-index-eq/): $G = U_J$ over $F$, the adelic group $G(\mathbb{A}) = G_\infty \times G_f$, the level subgroup $K_{\mathrm{set}} \subseteq G_f$, and the group $\Gamma = G(F)$ embedded diagonally. For the background see [adelic points](/learn/groups/#adelic-points-and-compact-open-subgroups).

### Multiplicity and the norm at infinity

**Definition 7.11.1 (Multiplicity).** For a set $\Omega \subseteq G(\mathbb{A})$ and $x \in G(\mathbb{A})$, the *multiplicity* of $\Omega$ at $x$ is
$$\operatorname{mult}(\Omega, x) = \sup_{y \in G(\mathbb{A})} \#\{\gamma \in \Gamma : x^{-1} \gamma y \in \Omega\}.$$

The multiplicity is the largest number of points of the orbit $\Gamma y$ that the translate $x\Omega$ can hold. It is monotone in $\Omega$, it is subadditive for finite unions, and right translation of $\Omega$ by $a$ does not change it after the change $y \mapsto y a$.

**Definition 7.11.2 (Norm at infinity).** For $g = (g_v) \in G_\infty$ put
$$\|g\|_\infty = \prod_{v \mid \infty} \|g_v\|_{\mathrm{op}},$$
the product of the operator norms at the infinite places. Let $n$ be the size of $J$, let $f = [F : \mathbb{Q}]$, and let $q_v$ be the integer attached to the infinite place $v$ by the Hida setting. The *nilradical exponent* is
$$N_1 = 4 n^2 \sqrt{2 \max_{v \mid \infty} q_v}.$$

**Definition 7.11.3 (Polynomial multiplicity).** The *polynomial multiplicity* holds if for all compact sets $\Omega, C \subseteq G(\mathbb{A})$ there is a constant $c$ such that
$$\operatorname{mult}\bigl(\Omega, x\,(g, 1)\bigr) \leq c\, \|g\|_\infty^{N_1} \quad \text{for all } x \in C,\ g \in G_\infty.$$

### Inputs

Let $\tau_1 : G(\mathbb{A}) \to \mathbb{R}$ be the size function of the reduction theory of Hermitian lattices, attached to the lattice $x L$ for $x \in G(\mathbb{A})$. For $r = (r_v)_{v \mid \infty}$ with $r_v \geq 0$ and a subgroup $K' \subseteq K_{\mathrm{set}}$ let $\operatorname{Om}(r, K')$ be the set of $(g_\infty, k)$ with $\|g_v\|_{\mathrm{op}} \leq r_v$ at each $v \mid \infty$ and $k \in K'$.

**Lemma 7.11.4 (Reduction theory).** If $n \geq 1$, the function $\tau_1$ is continuous and positive.

**Lemma 7.11.5 (Multiplicity from the lattice count).** Assume the lattice count and the triangle inequality for distances on $G_\infty$. Put $k = 4 n^2 f$. Then there is a constant $C_{\mathrm{Om}}(r) \geq 0$ such that for all $r \geq 0$, all $K' \subseteq K_{\mathrm{set}}$ and all $x$,
$$\operatorname{mult}\bigl(\operatorname{Om}(r, K'), x\bigr) \leq \frac{C_{\mathrm{Om}}(r)}{\tau_1(x)^{k}}.$$

**Lemma 7.11.6 (Translation of the size).** If $n \geq 1$, then for $x \in G(\mathbb{A})$ and $g \in G_\infty$,
$$\tau_1(x) \leq \tau_1\bigl(x (g, 1)\bigr)\, \|g\|_\infty^{1/f}.$$

**Lemma 7.11.7 (Norm power).** If $n \geq 1$, then $\|g\|_\infty^{4n^2} \leq \|g\|_\infty^{N_1}$ for all $g \in G_\infty$.

This holds since $\|g\|_\infty \geq 1$ for an element of a unitary group and $4n^2 \leq N_1$.

**Lemma 7.11.8 (Cover by boxes).** Each compact $\Omega \subseteq G(\mathbb{A})$ is covered by finitely many right translates $\operatorname{Om}(r, K')\, (1, a)^{-1}$, $a \in A$, with $r \geq 0$, a finite set $A \subseteq G_f$ and a subgroup $K' \subseteq K_{\mathrm{set}}$.

### The polynomial bound

**Theorem 7.11.9 (Polynomial multiplicity).** Assume the translation of the size, the norm power and the cover by boxes. Then the polynomial multiplicity holds.

Lean: `Formalism.L2.SG.Pf.multPoly_holds_of` (also `Formalism.L2.SG.Pf.multPoly_holds_of'`, with the norm power proved, and `Formalism.L2.SG.Pf.multPoly_holds_of''`, with the translation of the size also proved, so that only the cover by boxes is assumed).

*Proof.* Let $\Omega$ and $C$ be compact. Cover $\Omega$ by the boxes $\operatorname{Om}(r, K')(1, a)^{-1}$ for $a \in A$. If $C$ is empty there is nothing to prove. Otherwise the continuous positive function $\tau_1$ has a minimum $m > 0$ on $C$. Let $x \in C$, $g \in G_\infty$ and $y = x(g, 1)$. By monotonicity, subadditivity and right translation, and by the lemma on the lattice count,
$$\operatorname{mult}(\Omega, y) \leq \#A \cdot \frac{C_{\mathrm{Om}}(r)}{\tau_1(y)^{k}}.$$
The translation of the size gives $m \leq \tau_1(x) \leq \tau_1(y)\, \|g\|_\infty^{1/f}$, so
$$\tau_1(y)^{-k} \leq m^{-k}\, \|g\|_\infty^{k/f} = m^{-k}\, \|g\|_\infty^{4n^2}.$$
The norm power bounds $\|g\|_\infty^{4n^2}$ by $\|g\|_\infty^{N_1}$. So the claim holds with $c = \#A \cdot C_{\mathrm{Om}}(r) / m^{k}$. $\square$

### Folding the Poincaré series

Let $u$ be a word of the data, $S_{\mathrm{rat}} \subseteq G(\mathbb{A})$ the group of rational points of the Bessel subgroup for $u$, and $\Phi_T$ the Poincaré kernel attached to a test datum $T$. The *folding* for $u$ holds if two things are true. First, $S_{\mathrm{rat}}$ has a fundamental domain $\mathcal{F}_S$ in $G(\mathbb{A})$. Second, there are a compact set $\Omega_0 \ni 1$ and a constant $a$ such that for every test datum $T$: each compact $\Omega \supseteq \Omega_0$ gives a fold datum for $\Phi_T$ with constant $a$, and the multiplicity integral of $\Phi_T$ over each fundamental domain is finite for each compact $\Omega$.

We take five local statements as given.

1. *Level splitting.* If $n$ is in the unipotent part $N_f$ and $n h \in K_{\mathrm{set}}$, then $h \in K_{\mathrm{set}}$.
2. *Unipotent conjugation.* For $n \in N_f \cap K_{\mathrm{set}}$, the conjugate $x_u^{-1} n x_u$ lies in the second level subgroup $K_2$, and the level character $\chi_2$ takes on it the value $\psi_f(n)$.
3. *Rational Levi.* Each rational element of $S$ is a product $\nu \eta$ of a Levi part and a unipotent part.
4. *Product formula.* $\psi_\infty(\nu_\infty)\, \psi_f(\nu_f) = 1$ for the rational elements $\nu$.
5. *Unfolding.* If the polynomial multiplicity holds, the Bessel functions have their weighted decay, and the Poincaré kernel is well defined, then the multiplicity integral of $\Phi_T$ is finite for each compact $\Omega$ and each fundamental domain.

**Theorem 7.11.10 (Folding of the Poincaré series).** Assume the five statements for every Hida setting and every word. Then for every Hida setting, every word $u$ and every level character, if the Bessel functions have their weighted decay, the folding for $u$ holds.

Lean: `Formalism.L2.SG.Pf.foldOKC_holds_of`.

*Proof.* The fundamental domain of $S_{\mathrm{rat}}$ exists for every Hida setting. The level splitting, the unipotent conjugation, the rational Levi and the product formula show that the kernel $\Phi_T$ is invariant under $S_{\mathrm{rat}}$ on the left: a rational element $\nu\eta$ changes the kernel by $\psi_\infty(\nu_\infty)\psi_f(\nu_f) = 1$, and the unipotent part is absorbed by the level character. This gives the fold datum on each compact $\Omega \supseteq \Omega_0$. The polynomial multiplicity holds for every Hida setting, by the theorem above with its inputs proved, and with the weighted decay it gives the finiteness of the multiplicity integral through the unfolding. $\square$

**Remark 7.11.11 (Formalization).** The nilradical exponent $N_1$ depends on the maximum of the integers $q_v$ over the infinite places ([WuDecay.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/WuDecay.lean#L22)); it is not the exponent of the previous section. We did not unfold the size function $\tau_1$, the constant $C_{\mathrm{Om}}(r)$, the Poincaré kernel or the fold datum; the description of $\operatorname{Om}(r, K')$ as a box is our reading of its name. The norm power is proved in the second and third forms of the theorem; its proof from $\|g\|_\infty \geq 1$ is our reading. The fold datum step of the folding proof is our reading of the names of the five statements; we did not open the assembly lemma ([InHHClosed.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/InHHClosed.lean#L14)). The unfolding is stated as an implication with the polynomial multiplicity as its first premise ([InHHCut.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/InHHCut.lean#L322)).
