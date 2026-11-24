---
title: Height shells in a frame quotient
decls:
  - GlobalTheory.T.measure_heightShell_le_isotropicFrame_quotient
  - GlobalTheory.ResidueEisenstein.measure_shell_le
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Height shells in a frame quotient

This section bounds the volume of a height shell in a fundamental domain for the rational points of the stabiliser of an isotropic frame in an adelic unitary group. The shell of index $j$ is the set where the height lies between $e^{-(j+1)}$ and $e^{-j}$. Its volume grows at most like $e^{(n - (r+1)) j}$, where $n$ is the dimension of the hermitian space and $r + 1$ is the rank of the frame. The bound is used by [the frame bound for the spherical pole](/entry/sph-pole-frame-bound/) of Volume 12, where a sum over shells of a function of the height must converge. The proof moves each shell to one fixed slab by a flow in the centre of the Levi factor, and pays for the move with the modulus of the flow on the unipotent radical.

We use [unitary groups](/learn/groups/#unitary-groups), [adelic points](/learn/groups/#adelic-points-and-compact-open-subgroups), [Haar measure](/learn/analysis/#haar-measure) and [quotients of finite volume](/learn/groups/#quotients-of-finite-volume) of Volume 1.

Let $E / F$ be a CM extension of number fields with complex conjugation $\sigma$, and let $J$ be a nondegenerate hermitian $n \times n$ matrix over $E$. Let $G = \mathrm{U}(J)$ and let $G(\mathbb{A})$ be its adelic points, with $\mathbb{A} = \mathbb{A}_F \otimes_F E$ in the coefficients. A *Witt frame* of rank $r + 1$ is a pair $X, Y$ of $n \times (r+1)$ matrices over $E$ whose columns span two totally isotropic subspaces in duality under $J$. For $p \in G(\mathbb{A})$ and $\beta \in \mathrm{GL}_{r+1}(\mathbb{A})$ we say that $p$ *scales $X$ by $\beta$* if $p X = X \beta$. The elements that scale $X$ form the parabolic subgroup $P_X$ that stabilises the column span of $X$. Let $\Gamma_X = G(F) \cap P_X$ be its rational points.

Let $\Lambda$ be an $\mathcal{O}_E$-lattice in $E^n$ and $K_\Lambda \subseteq G(\mathbb{A})$ its level group. A *height* for the frame is a function $h : G(\mathbb{A}) \to \mathbb{R}$ such that each $g$ can be written $g = p k$ with $p$ scaling $X$ by some $\beta$ and $k \in K_\Lambda$, and then
$$h(p k) = |\det \beta|_{\mathbb{A}}.$$
For $j \in \mathbb{N}$ the *shell* of index $j$ is
$$S_j = \{ x \in G(\mathbb{A}) : e^{-(j+1)} < h(x) \leq e^{-j} \}.$$

**Theorem 7.4.1 (Shell volumes).** Let $E/F$ be CM, $J$ hermitian and nondegenerate, $(X, Y)$ a Witt frame of rank $r+1$, $\Lambda$ a lattice and $h$ a height for the frame as above. Let $\mu$ be a Haar measure on $G(\mathbb{A})$ and $D$ a measurable fundamental domain for $\Gamma_X$. Then there is a finite $B$ such that for all $j \in \mathbb{N}$,
$$\mu(D \cap S_j) \leq B\, e^{(n - (r + 1)) j}.$$

Lean: `GlobalTheory.T.measure_heightShell_le_isotropicFrame_quotient` (also `GlobalTheory.ResidueEisenstein.measure_shell_le`).

*Proof.* We use five facts about the frame, proved apart from this chapter.

1. There is a *Levi centre flow*: elements $b_j \in G(\mathbb{A})$, $j \in \mathbb{N}$, in the centre of the Levi factor of $P_X$, that commute with $\Gamma_X$ and scale $X$ by some $\beta_j$ with $h(b_j x) = e^{j} h(x)$ for all $x$.
2. The height is continuous, and it satisfies the scaling law $h(p x) = |\det \beta|_{\mathbb{A}}\, h(x)$ when $p$ scales $X$ by $\beta$.
3. The unipotent radical $N$ of $P_X$ has a Haar measure $\nu$ and a fundamental domain $D_N$ for $N(F)$ of mass one.
4. Conjugation by $b_j$ scales $\nu$ by the modulus $e^{-(n - (r+1)) j}$.
5. The group $\Gamma_X$ splits as a semidirect product of $N(F)$ and a lattice in a Levi group $M$, with a measure $\pi$ on $M$ and a fundamental domain $D_M$ of finite mass. The slab $\{ e^{-1} \leq h \leq 1 \}$ lies in $N M C$ for a compact set $C$.

A general lemma on semidirect lattices turns 3 to 5 into the following. There is a finite $B$ such that for each $b$ that commutes with $\Gamma_X$ and scales $\nu$ by a factor $\kappa$, and for each measurable $S$ with $b S \subseteq N M C$,
$$\kappa \cdot \mu(D \cap S) \leq B.$$
The proof of the lemma unfolds the integral of the indicator of a neighbourhood of $C$ over $D$ in two steps, first over $N(F) \backslash N(\mathbb{A})$ and then over the Levi part.

Fix $j$ and apply the lemma to $b = b_j$, $\kappa = e^{-(n - (r+1)) j}$ and $S = S_j$. The set $S_j$ is measurable since $h$ is continuous. Let $x \in S_j$. Then $h(b_j x) = e^j h(x)$ by facts 1 and 2. From $e^{-(j+1)} < h(x) \leq e^{-j}$ we get
$$e^{-1} = e^{j} e^{-(j+1)} \leq h(b_j x) \leq e^{j} e^{-j} = 1,$$
so $b_j x$ lies in the slab, and so in $N M C$. The lemma gives $e^{-(n - (r+1)) j} \mu(D \cap S_j) \leq B$. Multiply by $e^{(n - (r+1)) j}$. $\square$

**Remark 7.4.2 (Formalization).** The data of the frame are `DataJ` in [ScalesBy.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ScalesBy.lean#L17); its last two fields are the decomposition $g = pk$ and the formula for $h$. The five facts come from `T.exists_leviCentreFlow_wittFrame`, `T.isCompact_level_height_scales_isotropicFrame`, `unipRad_frame_closed_mass_one`, `T.leviCentreFlow_conj_scales_haar_isotropicUnipotent`, `T.rational_isotropicStabiliser_splitLattice` and `T.heightSlab_subset_unipotent_levi_compact`, and the lemma on semidirect lattices is `ResLine.modulus_mul_measure_shell_le` in [MeasureTranslateShellLeDivModulus.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/MeasureTranslateShellLeDivModulus.lean#L10). We read the statements of the five facts, not their proofs. Two of them return a first component that the proof drops with `-`. The bound is stated for the measure $\mu$ restricted to $D$, with values in $[0, \infty]$, and $B$ is a finite element of $[0, \infty]$. The statement asks for the frame $Y$ and the element $a$ only through the data of the frame.
