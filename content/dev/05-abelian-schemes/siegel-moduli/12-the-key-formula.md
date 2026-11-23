---
title: The key formula
decls:
  - GlobalTheory.KeyFam.keyFormula_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The key formula

A key input is a principally polarized abelian scheme with a rigidification, a theta section and a basis of tangent vectors, as in [the section on the Koszul complex](/entry/koszul-sections-exact-field/). The chapter on polarizations builds [a key rule for half characteristics](/entry/exists-key-rule-char-half/): a unit $\kappa(x)$ for every key input over a field of characteristic $0$, which behaves well under base change, is integral over discrete valuation rings and takes known values at the theta functions with half characteristics. This section states the *key formula*, which fixes $\kappa$ completely: its transformation law, its base change, its integrality, its value $1$ at the standard theta functions with half characteristics, and its absolute value at every complex point in terms of the norm of the theta function. Then it proves the formula. The key formula is an input of the proof at [the step on every character](/step/every-character-of-literature/). The background is [theta functions with characteristics](/learn/theta-functions-cm/#theta-functions-with-characteristics).

We use key inputs, holomorphic uniformizations and the theta functions $\vartheta[a,b](\tau, z)$ of [the section on holomorphy in the period matrix](/entry/ka-val-locally-holomorphic/). For a key input $x$ over $R$ write $(A, L)$ for its principally polarized abelian scheme of dimension $g \ge 1$, $r$ for the generator of $e^* L$, $\theta$ for the theta section and $v_1, \dots, v_g$ for the basis of tangent vectors.

**Definition 5.12.1 (Pullback of key inputs).** Let $f : R \to R'$ be a ring map, $x$ a key input over $R$ and $x'$ one over $R'$. Then $x'$ is a *pullback* of $x$ along $f$ if there are a map $\varphi : A' \to A$ over $\operatorname{Spec} f$ that makes $A'$ the base change of $A$ as a group scheme, and a generating isomorphism $w : L' \cong \varphi^* L$, such that the dimensions agree, $w$ carries $r'$ to the pullback of $r$, $w$ carries $\theta'$ to the pullback of $\theta$, and $\varphi \circ v'_i = v_i \circ \operatorname{Spec}(F)$ for the map $F : R[\varepsilon] \to R'[\varepsilon]$ that extends $f$ with $F(\varepsilon) = \varepsilon$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.KeyPB`.

For a complex key input $x$ with a holomorphic uniformization $u : \mathbb{C}^g \to A(\mathbb{C})$ we say that $u$ *matches* $r$ if the frame of $L$ at $0$ equals $r$; that $\theta$ *is given by* a function $\vartheta$ if $\theta \circ u = \vartheta \cdot (\text{frame})$; and that $v_i$ *is the direction* $w_i \in \mathbb{C}^g$ if the derivative of every function along $v_i$ is its derivative at $0$ in the direction $w_i$. A *hermitian form* for $u$ is a positive definite hermitian matrix $H$ with a character $\chi$ of the lattice $\Lambda = \ker u$ of absolute value $1$, such that the frames satisfy the functional equation of a theta function for $(H, \chi)$: $\operatorname{fr}(z) = \chi(\lambda) \exp\big(\pi H(z, \lambda) + \tfrac{\pi}{2} H(\lambda, \lambda)\big) \operatorname{fr}(z + \lambda)$ for $\lambda \in \Lambda$, where $H(z, w) = z \cdot H \bar w$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.HolUnif.IsRig`, `HolUnif.IsFn`, `HolUnif.IsDiff`, `HolUnif.IsAH`.

**Definition 5.12.2 (Key formula).** The *key formula* is the statement that there is a unit $\kappa(x) \in K^\times$, for every field $K$ of characteristic $0$ and every key input $x$ over $K$, with the following five properties.

1. *Transformation.* Let $x$ and $x'$ be key inputs over $K$ with the same $(A, L, r)$, with $\theta' = a \theta$ for some $a \in K$ and $v'_i = \sum_j M_{ij} v_j$ for a matrix $M$ over $K$. Then $a^8 \kappa(x') = \det(M)^4 \kappa(x)$.
2. *Base change.* If $f : K \to K'$ is a map of fields of characteristic $0$ and $x'$ is a pullback of $x$ along $f$, then $\kappa(x') = f(\kappa(x))$.
3. *Integrality.* Let $R$ be a [[discrete valuation ring|MGM3CNJW9V]] with fraction field $K$ of characteristic $0$, let $x$ be a key input over $R$ and $x_K$ a pullback of $x$ to $K$. Then there is a unit $u \in R^\times$ with $\kappa(x_K) = u$, and for every surjection $\rho : R \to k$ onto a field of characteristic $0$ and every pullback $x_k$ of $x$ along $\rho$, $\kappa(x_k) = \rho(u)$.
4. *Normalization.* Let $x$ be a key input over $\mathbb{C}$ with a holomorphic uniformization $u$ that matches $r$. Let $\tau$ be a symmetric complex $g \times g$ matrix with $\operatorname{Im} \tau$ [[positive definite|0QQCG3JWJ4]], and let $a, b \in \{0, \tfrac12\}^g$. Assume that $\ker u = \mathbb{Z}^g + \tau \mathbb{Z}^g$, that $\theta$ is given by $\vartheta[a,b](\tau, \cdot)$, where
$$\vartheta[a,b](\tau, z) = \sum_{n \in \mathbb{Z}^g} \exp\big(\pi i\, (n+a) \cdot \tau (n+a) + 2\pi i\, (n+a) \cdot (z + b)\big),$$
and that $v_i$ is the direction $(2\pi i)^{-1} e_i$. Then $\kappa(x) = 1$.
5. *Absolute value.* Let $x$ be a key input over $\mathbb{C}$ with a holomorphic uniformization $u$ that matches $r$ and a hermitian form $(H, \chi)$ for $u$. Let $\theta$ be given by $\vartheta$, let $v_i$ be the direction $W_i$, and let $F$ be a fundamental domain of $\Lambda$. Put
$$\begin{aligned} n_\theta &= \frac{1}{\operatorname{vol} F} \int_F |\vartheta(z)|^2 e^{-\pi \operatorname{Re} H(z, z)} \, dz, \\ n_\eta &= \frac{\operatorname{vol} F}{\pi^g |\det W|^2}. \end{aligned}$$
Then $|\kappa(x)| \, n_\theta^4 \, n_\eta^2 = (2\pi)^{2g}$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.KeyFormula`, `ReciprocityTheory.ChartRestriction.G.Geo.Tor.thetaChar`.

The five properties fit together. If $\theta$ is multiplied by $a$, then $n_\theta$ is multiplied by $|a|^2$; if $W$ is replaced by $M W$, then $n_\eta$ is divided by $|\det M|^2$. So property 5 is consistent with property 1. Property 5 determines $|\kappa|$ at every complex point, and property 4 fixes the phase at the standard points.

The proof goes through families. A complex key input is *normal at* $(\tau, M, a, b, c)$ if it has a uniformization with lattice $\mathbb{Z}^g + \tau \mathbb{Z}^g$ that matches $r$, with $\theta$ given by $c\, \vartheta[a,b](\tau, \cdot)$ and $v_i$ the direction $(2\pi i)^{-1} M_i$, as in [the section on the key invariant](/entry/ka-st/). By properties 1 and 4, the formula predicts the value $\det(M)^4 / c^8$ at such an input when $(a, b)$ is a half characteristic.

**Definition 5.12.3 (Connected families of key inputs).** *Key inputs lie in connected families* if for every key input $x$ over $\mathbb{C}$ there are a number field $k$, a [[smooth|EXKGG9X6J0]] $k$-algebra $S$ such that $K \otimes_k S$ is a domain for every field $K$ over $k$, a key input $y$ over $S$, a ring map $s : S \to \mathbb{C}$ along which $x$ is a pullback of $y$, a $k$-point $s_0 : S \to k$ and $t_0 \in k$, such that for every embedding $e : k \to \mathbb{C}$, every pullback $x_0$ of $y$ along $e \circ s_0$ is normal at some $(\tau, M, a, b, c)$ with $(a, b)$ a half characteristic, $c \ne 0$ and $e(t_0) = \det(M)^4 / c^8$.

Lean: `GlobalTheory.KeyKa.ConnFam`.

So every complex key input moves, inside a geometrically integral family over a number field, to a point where the predicted value is known and algebraic. A similar statement for polarized abelian varieties alone, without the theta section and the tangent basis, is the *polarized family* statement: every complex principally polarized abelian variety of dimension $g \ge 1$ is a fibre of a polarized family over a smooth geometrically integral algebra $R$ over a number field $K$, with a $K$-point whose fibres have potentially known key values.

Lean: `GlobalTheory.KeyFam.PolFam`, `GlobalTheory.KeyFam.GeomInt`, `GlobalTheory.KeyFam.PotKnown`, `GlobalTheory.KeyFam.Known`.

**Theorem 5.12.4 (The key formula).** The key formula holds.

Lean: `GlobalTheory.KeyFam.keyFormula_holds`.

*Proof.* The proof has three steps.

First, polarized families exist. This follows from the laws, the second laws, the uniformization theorem for complex abelian varieties and the algebraicity of tori, by a lemma on polarized families.

Second, key inputs lie in connected families. This follows from the first step, the laws and the second laws, by a lemma that adds a rigidification, a theta section and a basis of the Lie algebra to a polarized family, so that the given complex key input is a fibre and the fibres at the $k$-point are normal at half characteristics.

Third, connected families give the key formula. Take the key rule for half characteristics, from the laws, the uniformization theorem, the theta inversion formula, the Koecher statement and the algebraicity of tori. It gives a unit $\kappa$ with the transformation, base change and integrality properties, normalized at half characteristics. Its values specialize along families: if $y$ is a key input over a geometrically integral smooth algebra $S$, then the value of $\kappa$ at a complex point of $S$ and at the $k$-point $s_0$ are linked by the family, and the value at $s_0$ is $\det(M)^4 / c^8$ by the normalization. The value is equivariant under the action of $\operatorname{Aut}(\mathbb{C})$, and key inputs descend to countable subrings. With these facts, and the base change of polarizations, a lemma on key rules and families shows that the key rule satisfies all five properties. $\square$

**Remark 5.12.5.** Property 3 has two parts. The first part, the existence of a unit $u \in R^\times$, is a real statement also for discrete valuation rings with residue field of characteristic $p > 0$, and it is the part that the later chapters use at primes $p$. The second part speaks only of surjections onto fields of characteristic $0$. For a discrete valuation ring with residue characteristic $p$ there is no such surjection, so the second part is empty in that case.

**Remark 5.12.6 (Formalization).** The theorem is a term: `keyFormula_of_connFam` applied to `KeyFam.connFam_of_polFam`, applied to `KeyFam.polFam` ([ExactKeyFormulaProof.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExactKeyFormulaProof.lean#L28)). The laws come from `abelianSchemeLaws_all`, while `keyFormula_of_connFam` takes its laws from `T.abelianScheme_laws_unconditional` ([KeyFormulaOfConnFam.lean](lean:Development/AbelianVarietyTheory/Proofs/UniformizationProofs/KeyFormulaOfConnFam.lean#L35)); the uniformization theorem enters as `thetaUnifAV_closed` in one place and as `T.theta_uniformisation_complex_abelian_varieties` in the other. The third step uses `KeyTop.exists_keyRule_charHalf`, `KeyRoot.keyFormula_of_families`, `T.keyData_descend_countable_subrings`, `ThetaFrameSpec.value_specialises` and `ThetaEquiv.val_equivariant`; we followed their statements, and the description of the first two steps is a reading of the statements of `polFam` and `connFam_of_polFam`, whose proofs we did not open. The statement `ConnFam` is also proved a second time, as `connFam_holds` in `ConnFamHolds.lean` through `T.keyDatumConnectedFamily_of_polarizedArithmeticFamily`; that file is imported here but its theorem is not used. The name `KeyFormula` is also used for a different definition in [CubicWedgeNormPeriods.lean](lean:Development/AbelianVarietyTheory/BlockTheory/CMModuli/CubicWedgeNormPeriods.lean#L92). The second part of property 3 is the vacuous case noted above: it quantifies over `CharZero` residue fields only ([IsLieBasis.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/IsLieBasis.lean#L127)).
