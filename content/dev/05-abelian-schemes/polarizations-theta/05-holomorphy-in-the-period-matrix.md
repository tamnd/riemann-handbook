---
title: Holomorphy in the period matrix
decls:
  - GlobalTheory.KeyKa.KaHol.kaVal_locally_holomorphic
  - GlobalTheory.T.koszulInvariant_locally_holomorphic_periodMatrix
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Holomorphy in the period matrix

This section shows that over the complex numbers the key value of the previous section is a holomorphic function of the period matrix $\tau$, locally on the Siegel space, when the theta section is the theta function with a half characteristic. Together with the independence of the sections, proved later, this makes the key invariant a holomorphic function on the Siegel space. It is used in [the key invariant theorem](/entry/ka-st/) for the property of holomorphy. The background is [holomorphic functions](/learn/complex-analysis/#holomorphic-functions), [Poisson summation, theta and Mellin](/learn/complex-analysis/#poisson-summation-theta-and-mellin) and [Siegel moduli schemes and level structures](/learn/abelian-varieties/#siegel-moduli-schemes-and-level-structures).

Let $\mathfrak{H}_g$ be the Siegel space of symmetric complex $g \times g$ matrices $\tau$ with $\operatorname{Im}\tau$ positive definite. For $a, b \in \mathbb{C}^g$ the *theta function with characteristic* $(a, b)$ is
$$\theta\begin{bmatrix} a \\ b \end{bmatrix}(\tau, z) = \sum_{k \in \mathbb{Z}^g} \exp\bigl(\pi i\, (k + a)^{T} \tau (k + a) + 2\pi i\, (k + a)^{T}(z + b)\bigr).$$
The characteristic is a *half characteristic* if every $a_i$ and every $b_i$ is $0$ or $\tfrac12$.

**Definition 2.5.1 (Theta functions of level l).** Let $\tau \in \mathfrak{H}_g$, $a, b \in \mathbb{C}^g$ and $l \in \mathbb{N}$. An entire function $F$ on $\mathbb{C}^g$ is a *theta function of level* $l$ for $(\tau, a, b)$ if for all $m, k \in \mathbb{Z}^g$
$$F(z + m + \tau k) = \exp\Bigl(2\pi i\bigl(a^{T}m - b^{T}k - \tfrac12 k^{T}\tau k - k^{T} z\bigr)\Bigr)^{l} F(z).$$
A family $F(p, z)$ is *holomorphic* on a set $W$ of complex $g \times g$ matrices if it is holomorphic in $(p, z)$ on a neighbourhood of each point of $W \times \mathbb{C}^g$. A *holomorphic level basis* is a family $B_1, \dots, B_N$ of functions $B_k(p, z)$, holomorphic on the set $\mathcal{D}_g$ defined below, such that for each $p \in \mathcal{D}_g$ the $B_k(p, \cdot)$ are a basis of the theta functions of level $l$ for $(\tfrac12(p + p^{T}), a, b)$.

Lean: `GlobalTheory.KeyKa.IsLevel`, `GlobalTheory.KeyKa.HolFam`, `GlobalTheory.KeyKa.LevBasis`.

The function $\theta[a; b](\tau, \cdot)$ is a theta function of level $1$ for $(\tau, a, b)$. A section of $L^l$ on a complex torus with the line bundle of $\theta$ is the same as a theta function of level $l$.

We work with all complex matrices $p$, not only symmetric ones, and use the symmetrization $\tau(p) = \tfrac12(p + p^{T})$. Let
$$\mathcal{D}_g = \{p \in M_g(\mathbb{C}) : \tau(p) \in \mathfrak{H}_g\}.$$
This is an open subset of $\mathbb{C}^{g \times g}$, and a function $H$ on $\mathfrak{H}_g$ is *holomorphic on the Siegel space* if $p \mapsto H(\tau(p))$ is holomorphic on $\mathcal{D}_g$. For symmetric arguments this is the usual notion, since $\tau$ is a holomorphic retraction of $\mathcal{D}_g$ onto $\mathfrak{H}_g$.

Lean: `ReciprocityTheory.ChartRestriction.G.Key.phDom`, `ReciprocityTheory.ChartRestriction.G.Key.IsHoloSiegel`.

**Definition 2.5.2 (Uniformization and theta witness).** Let $(A, L)$ be a principally polarized abelian variety over $\mathbb{C}$ of dimension $g$. A *uniformization* is a surjective homomorphism $u : \mathbb{C}^g \to A(\mathbb{C})$ with discrete kernel $\Lambda$. Let $x$ be a key input over $\mathbb{C}$ with abelian variety $A$, and let $\tau \in M_g(\mathbb{C})$ and $a, b \in \mathbb{C}^g$. Then $(x, u)$ is a *theta witness* at $(\tau, a, b)$ if $\tau$ is symmetric with $\operatorname{Im}\tau$ positive definite, $\Lambda = \mathbb{Z}^g + \tau\mathbb{Z}^g$, $u$ is compatible with the rigidification $r$, the section $\theta$ corresponds under $u$ to the function $\theta[a; b](\tau, \cdot)$, and the tangent vector $v_i$ corresponds to $(2\pi i)^{-1} e_i$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.HolUnif`, `GlobalTheory.KeyKa.Wit`, `ReciprocityTheory.ChartRestriction.G.Geo.Tor.thetaChar`.

We take as given the complex uniformization of principally polarized abelian varieties: every principally polarized abelian variety $(A, L)$ over $\mathbb{C}$ with a rigidification has a uniformization compatible with it, under which $L$ is the line bundle of Appell-Humbert data, sections of $L^l$ are theta functions for those data, tangent vectors are constant vector fields, endomorphisms lift to linear maps, and the Weil pairing is the imaginary part of the hermitian form (D. Mumford, *Abelian Varieties*, §1 to §3; see also [the complex uniformization](/learn/abelian-varieties/#the-complex-uniformization)). We call this *the uniformization theorem*.

**Theorem 2.5.3 (Local holomorphy of the key value).** Assume the laws and the uniformization theorem. Let $g \geq 1$, let $(n, l, l', \alpha)$ be admissible for $g$, and let $(a, b)$ be a half characteristic. Let $p_0 \in \mathcal{D}_g$. Let $x_0$ be a key input over $\mathbb{C}$ of dimension $g$, with a uniformization $u_0$ such that $(x_0, u_0)$ is a theta witness at $(\tau(p_0), a, b)$, and assume that some sections $s_0$ of $L^n$ have a key value $\kappa_0$. Then there are an open set $W$ with $p_0 \in W \subseteq \mathcal{D}_g$ and a holomorphic function $V$ on $W$ with the following property. For every $p \in W$, every key input $x$ over $\mathbb{C}$ of dimension $g$ and every uniformization $u$ such that $(x, u)$ is a theta witness at $(\tau(p), a, b)$, there are sections $s$ of $L^n$ with a key value $\kappa$ such that $\kappa = V(p)$.

Lean: `GlobalTheory.KeyKa.KaHol.kaVal_locally_holomorphic` (also `GlobalTheory.T.koszulInvariant_locally_holomorphic_periodMatrix`, a second name).

*Proof.* Through $u_0$ the sections $s_{0,i}$ are theta functions $F_{0,i}$ of level $n$ for $(\tau(p_0), a, b)$, and the transversal zeros of $s_0$ in the key value $\kappa_0$ give $d = g!\, n^g$ simple common zeros $z_{0,a} \in \mathbb{C}^g$, one in each class modulo $\Lambda$. Since $n \geq 4 \geq 1$, there is a holomorphic level basis $B_1, \dots, B_N$ of level $n$ on all of $\mathcal{D}_g$, made from theta functions with characteristics. Write $F_{0,i} = \sum_k T_{ik} B_k(p_0, \cdot)$ and put
$$F_i(p, z) = \sum_k T_{ik} B_k(p, z).$$
Each $F_i$ is holomorphic in $(p, z)$. By the implicit function theorem, the simple zeros $z_{0,a}$ move holomorphically: on a neighbourhood $W$ of $p_0$ there are holomorphic $z_a(p)$ with $F_i(p, z_a(p)) = 0$ and nonvanishing Jacobian. For $p$ near $p_0$ the $z_a(p)$ stay distinct modulo $\mathbb{Z}^g + \tau(p)\mathbb{Z}^g$, since the lattice coordinates of $z_a(p) - z_b(p)$ move continuously and are not integers at $p_0$. They are also all the common zeros modulo the lattice. Indeed, every class has a representative $\sum_i x_i e_i + \sum_i y_i \tau(p) e_i$ with $(x, y) \in [0, 1]^{2g}$, a compact set. If common zeros outside the $z_a(p)$ existed for $p$ arbitrarily close to $p_0$, a limit point would be a common zero at $p_0$, hence congruent to some $z_{0,a}$, and this contradicts the uniqueness in the implicit function theorem near $z_{0,a}$. Shrink $W$ so that these properties hold on $W$.

Next, for $p \in W$ the bases of theta functions of the levels $l - jn$ and $l' - jn$ can be chosen holomorphically in $p$. Then the matrices of multiplication by the $F_i$ are holomorphic in $p$, and so are the evaluation matrices at the $z_a(p)$ and the theta comparison constants $\lambda_j(p)$, $\lambda'_j(p)$, which are built from $\theta[a; b](\tau(p), \cdot)$. The square torsion of a holomorphic family of acyclic based complexes is holomorphic: a contraction can be chosen holomorphically near each point, and the torsion does not depend on the contraction. The Jacobian factor is $J(p) = \prod_a \det\bigl((2\pi i)^{-1} \partial F_i/\partial z_k\bigr)(p, z_a(p))$, since $v_k$ corresponds to $(2\pi i)^{-1} e_k$. Define $V(p)$ by the formula for the key value in these holomorphic data. Then $V$ is holomorphic on $W$, since all the units are holomorphic and nonzero.

Finally let $p \in W$ and let $(x, u)$ be a theta witness at $(\tau(p), a, b)$. Through $u$, the functions $F_i(p, \cdot)$ are sections $s_i$ of $L^n$, the points $u(z_a(p))$ are transversal zeros, and the bases and comparisons transport to $x$. So $s$ has the key value $V(p)$, by the uniqueness of the square torsion. $\square$

**Remark 2.5.4.** The theorem does not say that the key value at $\tau(p)$ is unique. That comes from the independence of the sections, proved in [the section on independence](/entry/key-invariant-independent-of-sections/). The two together give a single holomorphic function of $\tau$ on $\mathfrak{H}_g$, and this is how the holomorphy property of the key invariant is proved.

**Remark 2.5.5 (Formalization).** The uniformization theorem is the hypothesis `ThetaUnifAV` ([ThetaUnifAV.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/ThetaUnifAV.lean#L29)). The proof is in [KoszulInvariantLocallyHolomorphicPeriodMatrix.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/KoszulInvariantLocallyHolomorphicPeriodMatrix.lean#L534); its steps are the lemmas `exists_simpleZeros`, `LevelBasis.exists_levBasis`, `HolZeros.simple_zeros_move_holomorphically`, `exists_data` and `TorsionHolomorphic.exists_differentiableOn_torsSq`, whose statements we followed; we did not read each of their proofs. The second name is proved by a `first | exact … | …` block, under a raised heartbeat limit, whose later alternatives are never reached ([KoszulInvariantLocallyHolomorphicPeriodMatrixStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/KoszulInvariantLocallyHolomorphicPeriodMatrixStatement.lean#L21)). The period variable is a general matrix $p$ and only its symmetrization enters, so the statement is about functions on $\mathcal{D}_g$, not on $\mathfrak{H}_g$.
