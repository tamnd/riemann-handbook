---
title: Key rules at the archimedean place
decls:
  - GlobalTheory.MBLow.ArchProof.exists_cd
  - GlobalTheory.MBLow.ArchProof.arch_of_rule4
  - GlobalTheory.T.keyRule_complex_existence_jets_key_value
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Key rules at the archimedean place

This section proves that a key rule with four basic properties has an archimedean property. The property says this: near the boundary of a degenerating family, the theta jets of the family converge, and their sums are the theta jets of a complex abelian variety. That complex abelian variety has the same key value as the abelian part of the family. The result is one of the inputs below [the record for every character](/step/every-character-of-literature/). Two later proofs pass it to the archimedean existence theorem for fields isomorphic to $\mathbb{C}$. The background is in [theta functions with characteristics](/learn/theta-functions-cm/#theta-functions-with-characteristics) and [semi-abelian degenerations](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction).

For a symmetric complex $g \times g$ matrix $\tau$ with $\operatorname{Im}\tau$ positive definite and $a, b \in \mathbb{C}^g$, let $\vartheta[a, b](z, \tau)$ be the theta function with characteristic $(a, b)$. A vector $a$ is *half-integral* if each $a_i$ is $0$ or $\tfrac12$.

**Definition 1.7.1 (key rule).** A *key input* over a ring $S$ is a polarized abelian scheme $P$ over $S$ of relative dimension $g \geq 1$, with a rigidification, a theta section $\theta$ and a basis $v = (v_1, \dots, v_g)$ of the Lie algebra. A *key rule* $\kappa$ gives a unit $\kappa(x) \in K^\times$ for each field $K$ of characteristic $0$ and each key input $x$ over $K$.

**Definition 1.7.2 (four rules).** A key rule $\kappa$ *satisfies the four rules* if it has these properties.

1. *Homogeneity.* Let $x$ and $x'$ be key inputs over $K$ on the same $P$. If $\theta' = a\theta$ with $a \in K$ and $v'_i = \sum_j M_{ij} v_j$, then $a^8 \kappa(x') = (\det M)^4 \kappa(x)$.
2. *Base change.* If $f : K \to K'$ is a ring map and $x'$ is the pullback of $x$ along $f$, then $\kappa(x') = f(\kappa(x))$.
3. *Value one.* Let $x$ be a key input over $\mathbb{C}$ with a holomorphic uniformization of lattice $\mathbb{Z}^g + \tau\mathbb{Z}^g$. If the rigidification is the standard one, the theta section is $\vartheta[a, b](z, \tau)$ with $a, b$ half-integral, and $v_i$ is $(2\pi i)^{-1}\partial/\partial z_i$, then $\kappa(x) = 1$.
4. *Units in families.* Let $S$ be an integrally closed Noetherian domain of characteristic $0$ and $y$ a key input over $S$. Then there is a unit $u \in S^\times$ such that $\kappa(x) = f(u)$ for each field $K$ of characteristic $0$, each ring map $f : S \to K$ and each pullback $x$ of $y$ along $f$.

**Definition 1.7.3 (classical data).** Let $B$ be the abelian part of a degeneration over $\mathbb{C}$, of dimension $g'$. *Classical data* for $B$ consist of a symmetric $\tau$ with $\operatorname{Im}\tau$ positive definite, half-integral $a, b \in \mathbb{C}^{g'}$, a number $c \neq 0$, a surjective homomorphism $\operatorname{ex} : \mathbb{C}^{g'} \to B(\mathbb{C})$ with kernel $\mathbb{Z}^{g'} + \tau\mathbb{Z}^{g'}$, and a factor $\operatorname{fr}(z) \in \mathbb{C}^\times$ with $\operatorname{fr}(0) = 1$ and the automorphy law of $\vartheta[a, b]$, such that
$$\theta_B(\operatorname{ex} z) = c\,\vartheta[a, b](z, \tau)\operatorname{fr}(z).$$
Let $X$ be the character group of the torus part, with a basis $b_1, \dots, b_r$. *Toric classical data* add a $g' \times r$ matrix $t_{12}$, a symmetric $r \times r$ matrix $t_{22}$ and a half-integral $b_2 \in \mathbb{C}^r$, such that the extension class is $c(\chi) = \operatorname{ex}(t_{12}\chi)$ and
$$\psi(\chi)\operatorname{fr}(t_{12}\chi) = \exp\bigl(\pi i\, \chi^{\mathsf T} t_{22}\chi + 2\pi i\, \chi^{\mathsf T} b_2\bigr)$$
for $\chi \in X$, written in the basis $b_l$.

*Classical data are good for $\kappa$* if the following holds. For each Lie basis $v^B$ of the abelian part, each $g' \times g'$ matrix $M^B$ such that the tangent vector over $v^B_i$ has the coordinate vector $(2\pi i)^{-1}M^B_i$, and each value $k_0$ of $\kappa$ on the abelian part with $v^B$, we have $\det M^B \neq 0$ and $k_0 c^8 = (\det M^B)^4$.

**Definition 1.7.4 (archimedean property).** A key rule $\kappa$ has the *archimedean property* if the following holds. Let $R$ be a Noetherian local domain with an embedding $\operatorname{Frac} R \to \mathbb{C}$, and let $D$ be degeneration data over $R$ with abelian part of dimension $g'$ and character group $X$ of rank $r$. Let $g = g' + r \geq 1$, let $m$ be odd and $k$ a multiple of $m^2$. Let $\beta$ be a form of level $k$ on $X$, and let $q$ be a level structure of level $m^2$ with root of unity $\zeta$. Let $s_a$ be families of sections, indexed by $a \in (\mathbb{Z}/m^2)^{2g}$, whose coefficients live on the coset of $q(a)$ in $X/mX$. Let $\gamma_1, \dots, \gamma_g$ be tangent points adapted to a Lie basis $v^B$ and to the basis of $X$. Let $k_0$ be the value of $\kappa$ on the abelian part. Write $c_{a,j}(\alpha) = c'_{a,j}(\alpha) + \epsilon\, c''_{a,j}(\alpha)$ for the jet of $s_a$ at $\gamma_j$ in degree $\alpha \in X$, a dual number, and
$$e(\alpha) = \max\bigl(0, \lfloor \beta(\alpha, \alpha)/2m^2 \rfloor\bigr).$$
Then there is $\varepsilon > 0$ such that for each $u$ with $0 < |u| < \varepsilon$:

1. the series $\sum_\alpha c'_{a,j}(\alpha) u^{e(\alpha)}$ and $\sum_\alpha c''_{a,j}(\alpha) u^{e(\alpha)}$ converge absolutely;
2. there are a key input $x_0$ over $\mathbb{C}$ of dimension $g$ and a level structure on $x_0$ of level $m^2$ with root of unity $\zeta$ whose theta jets at the level points have the values $\rho^{-m^2}\sum_\alpha c'_{a,j}(\alpha) u^{e(\alpha)}$ and the first derivatives $\rho^{-m^2}\sum_\alpha c''_{a,j}(\alpha) u^{e(\alpha)}$, up to a multiple of the value in each direction;
3. $\kappa(x_0) = k_0$.

Here $\rho$ is the value of the rigidification of $D$ at the origin.

**Lemma 1.7.5 (classical data for a degeneration).** Let $\kappa$ satisfy the four rules. Let $R$ and $D$ be as in the archimedean property, and fix a basis of $X$. Then there are toric classical data for $D$ with the holomorphic structure of the abelian part, and these data are good for $\kappa$.

Lean: `GlobalTheory.MBLow.ArchProof.exists_cd`.

*Proof.* First we find classical data for the abelian part that are good for $\kappa$. If $g' = 0$, the case of dimension zero gives them. If $g' \geq 1$, the classical theta description of the abelian part gives them; this step uses the four rules. The data have a cubical structure and a symmetry, which come from the holomorphic structure. With these two facts, the normal form for the period frame extends the data to toric classical data with the fixed basis of $X$. $\square$

**Theorem 1.7.6 (archimedean property of key rules).** Let $\kappa$ be a key rule that satisfies the four rules. Then $\kappa$ has the archimedean property.

Lean: `GlobalTheory.T.keyRule_complex_existence_jets_key_value` (also `GlobalTheory.MBLow.ArchProof.arch_of_rule4`, a second name).

*Proof.* Fix the data of the archimedean property.

*Classical data.* The lemma gives toric classical data $(\tau, a, b, c, t_{12}, t_{22}, b_2)$ that are good for $\kappa$. Let $\sigma$ be the bijection between $\{1, \dots, g\}$ and the abelian and toric directions. For a $r \times r$ matrix $S$, let $\tau_{\mathrm{full}}(S)$ be the block matrix
$$\tau_{\mathrm{full}}(S) = \begin{pmatrix} \tau & t_{12} \\ t_{12}^{\mathsf T} & t_{22} + S \end{pmatrix},$$
reordered by $\sigma$. Let $a_F$ be $a$ in the abelian directions and $0$ in the toric directions, and let $b_F$ be $b$ and $b_2$.

*The Lie matrix.* For each $j$, the adapted point $\gamma_j$ gives a vector $Z_j \in \mathbb{C}^g$ and a constant $c_{0,j}$. In an abelian direction, the abelian part of $Z_j$ is the derivative of $\gamma_j$ in the coordinates. In a toric direction $l$, the abelian part is $0$ and the toric part is the unit vector $e_l$. For each holomorphic $F$ with $f(\alpha)\, s(\alpha) = \operatorname{fr}^k F$ at the points of the family, we get
$$\begin{aligned}
c'_{j}(\alpha)/\rho^k &= F(0), \\
c''_{j}(\alpha)/\rho^k &= dF(0)(Z_j) + k\, c_{0,j} F(0).
\end{aligned}$$
Let $M_x$ have the rows $2\pi i\, Z_j$. The matrix is block triangular with the identity in the toric block. So $\det M_x = \det M^B$, where $M^B$ is the abelian block. Since the data are good for $\kappa$, $\det M_x \neq 0$ and $k_0 c^8 = (\det M_x)^4$.

*Labels and positivity.* The level structure $q$ has integral labels: vectors $M(a), N(a) \in \mathbb{Z}^g$ such that $q(a)$ is the image of $(m^2)^{-1}(M(a) + \tau_{\mathrm{full}}(0) N(a))$. These labels are additive modulo $m^2$, and the pairing of $q$ is $\zeta$ to the standard symplectic form. Let $B_\beta$ be the matrix of $\beta$ in the basis of $X$. There is $T$ such that, for $\operatorname{Im} w > T$, $\tau_{\mathrm{full}}(wB_\beta)$ is symmetric with positive definite imaginary part. The term of each theta series at $\tau_{\mathrm{full}}(wB_\beta)$ is the term at $\tau_{\mathrm{full}}(0)$ times $e^{2\pi i w\, e(y + m\chi)}$, where $y$ is the toric part of $N(a)$ in $X$.

*Convergence.* Let $\varepsilon = e^{-2\pi T}$. For $0 < |u| < \varepsilon$, there is $w$ with $\operatorname{Im} w > T$ and $e^{2\pi i w} = u$. The coefficients of $s_a$ vanish off the coset $y + mX$. On that coset, the jet formula with $F$ the term of index $\chi$ gives the terms of the translated theta series
$$\vartheta_a(z) = \phi_a(z)\,\vartheta[a_F, b_F]\bigl(mz + m^{-1}(M(a) + \tau_{\mathrm{full}} N(a)), \tau_{\mathrm{full}}\bigr),$$
with $\tau_{\mathrm{full}} = \tau_{\mathrm{full}}(wB_\beta)$ and an exponential factor $\phi_a$. The series of terms and the series of their derivatives converge absolutely. Thus
$$\begin{aligned}
\rho^{-m^2}\sum_\alpha c'_{a,j}(\alpha) u^{e(\alpha)} &= c\,\vartheta_a(0), \\
\rho^{-m^2}\sum_\alpha c''_{a,j}(\alpha) u^{e(\alpha)} &= c\, d\vartheta_a(0)(V_j) + m^2 c_{0,j}\, c\,\vartheta_a(0),
\end{aligned}$$
with $V_j = (2\pi i)^{-1}(M_x)_j$. Since $\rho \neq 0$, the series without the factor $\rho^{-m^2}$ converge absolutely too.

*The complex abelian variety.* Since $\tau_{\mathrm{full}}$ is symmetric with positive definite imaginary part, $a_F$ and $b_F$ are half-integral, $c \neq 0$ and $\det M_x \neq 0$, there is a key input $x_0$ over $\mathbb{C}$ of dimension $g$ in normal form. Its lattice is $\mathbb{Z}^g + \tau_{\mathrm{full}}\mathbb{Z}^g$, its theta section is $c\,\vartheta[a_F, b_F]$, and its Lie basis is $V_j$. The labels give a level structure on $x_0$ of level $m^2$ with root of unity $\zeta$. Its level points are the images of $(m^2)^{-1}(M(a) + \tau_{\mathrm{full}}N(a))$. The theta jets of a key input in normal form at these points are the values $c\,\vartheta_a(0)$ and the derivatives along $V_j$, up to a multiple of the value. This gives part 2.

*The key value.* Homogeneity and the value one rule give $\kappa(x_0) c^8 = (\det M_x)^4$ for a key input in normal form. With $k_0 c^8 = (\det M_x)^4$ and $c \neq 0$, we get $\kappa(x_0) = k_0$. $\square$

**Remark 1.7.7 (Formalization).** The first name is proved from the second by `first | exact @…`. Inside the main proof, the last step uses only homogeneity and the value one rule ([KeyRuleComplexExistenceJetsKeyValue.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KeyRuleComplexExistenceJetsKeyValue.lean#L198)). Base change and units in families enter only through the classical theta description of the abelian part. The Lie matrix step is the lemma `exists_vec` of the same file. We did not unfold the data types `DegPre`, `NumD`, `NumOf`, `Fam`, `GtPt`, `Form` and `KeyIn`, the conditions `PsiEven`, `TauBimult`, `QLevel`, `IsEvFam`, `Adapted` and `BKey`, the jet `jc`, the holomorphic structure `Geo` and the theta jet predicate `ThJet`. We did not open the proofs of `DimZero.main`, `exists_classicalThetaDescription_abelianPart`, `PsiFrame.exists_cd`, `jet_family_deriv`, `exists_integral_labels`, `full_posDef`, `term_smul_bmat`, `term_sum_and_fderiv`, `exists_keyIn_nf`, `exists_level_of_labels`, `thJet_of_normalForm` and `key_value_of_nf`. The exponent $e(\alpha)$ is the integer quotient of $\beta(\alpha, \alpha)$ by $2m^2$, cut off at $0$ by `toNat`.
