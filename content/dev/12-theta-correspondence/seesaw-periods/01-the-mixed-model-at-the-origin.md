---
title: The mixed model at the origin
decls:
  - GlobalTheory.LeviOrigin.value_at_origin
  - GlobalTheory.T.weilRepresentation_value_at_origin_leviFactor
  - GlobalTheory.MixSourceFormulas.mixed_source
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The mixed model at the origin

A Witt decomposition $S = X \oplus S_0 \oplus Y$ of a Hermitian space gives a parabolic subgroup of $U(S)$ with Levi factor $\mathrm{GL}(X) \times U(S_0)$. The Weil representation of $U(S) \times U(T)$ restricts to this parabolic in a simple way when one passes to a mixed model. This section proves the formulas of that restriction in the model of theta functions. The main result is the Levi formula at the origin: the Levi factor $\mathrm{GL}(X)$ acts on the mixed coordinate at $0$ by the character $\chi_T(\det a)^{-1} |\det a|_E^{n/2}$. The formulas feed the evaluation and flat maps of the next sections, and through them the step [every character from the literature](/step/every-character-of-literature/).

**Definition 7.1.1 (Weil datum).** Let $E/F$ be the CM extension of the datum and let $\xi_0 \in E$ be its fixed element. Let $S$ and $T$ be nondegenerate Hermitian spaces over $E$ with Gram matrices $J_S$ and $J_T$, of dimensions $m$ and $n$. Put $W(S, T) = M_{n \times m}(\mathbb{A}_E)$, with the symplectic form

$$\begin{aligned} \langle x, y \rangle &= \mathrm{Tr}_{\mathbb{A}_E/\mathbb{A}}\bigl(\xi_0 \, \mathrm{tr}(J_S^{-1} y^{*} J_T x)\bigr). \end{aligned}$$

The group $U(S)(\mathbb{A}) \times U(T)(\mathbb{A})$ acts on $W(S, T)$ by $(g, h) \cdot x = h x g^{-1}$. For $w_0 \in W(S, T)$ and a function $f$ on $W(S, T)$, the Heisenberg operator is $(H(w_0) f)(w) = \psi(\tfrac12 \langle w, w_0 \rangle) f(w + w_0)$. A theta function is a continuous function $f$ on $W(S, T)$, smooth in the real directions, with $f(\gamma + w) = \psi(-\tfrac12 \langle \gamma, w \rangle) f(w)$ for every rational $\gamma \in M_{n \times m}(E)$, and fixed by $H(w)$ for all $w$ in an open subgroup of the finite part. A Weil datum on $(S, T)$ is a homomorphism $\omega$ from $U(S)(\mathbb{A}) \times U(T)(\mathbb{A})$ to the linear operators on functions on $W(S, T)$, with Hecke characters $\chi_S, \chi_T$ of $\mathbb{A}_E^{\times}$, such that: $\psi$ is the standard character; $\chi_S$ and $\chi_T$ restrict to the quadratic character of $E/F$ on $\mathbb{A}^{\times}$; $\omega$ preserves theta functions; $\omega(g, h) H(w) = H((g, h) \cdot w)\, \omega(g, h)$; $\omega(\gamma, \gamma') f (0) = f(0)$ for rational $\gamma, \gamma'$; the action is continuous and unitary for the inner product on a fundamental domain; and at the split places the action of the Levi factors in the local models is given by $\chi_S$ and $\chi_T$.

These are the properties of the global [Weil representation](/learn/theta/#the-weil-representation) in the model of theta functions: the value $f \mapsto \omega(g, h) f(0)$ is the theta distribution, and the Hecke characters fix the splitting of the metaplectic cover over the unitary groups.

**Definition 7.1.2 (Witt decomposition).** A Witt decomposition of depth $\rho$ of $S$ is a decomposition $S = X \oplus S_0 \oplus Y$, where $X$ and $Y$ are isotropic of dimension $\rho$, the pairing between $X$ and $Y$ is perfect, and $S_0$ is orthogonal to $X \oplus Y$. In coordinates it is given by matrices $e, e'$ of size $m \times \rho$ and an embedding $i_0$ of $S_0$ with $e^{*} J_S e = 0$, $e'^{*} J_S e' = 0$, $e'^{*} J_S e = 1$, $i_0^{*} J_S i_0 = J_{S_0}$, $i_0^{*} J_S e = i_0^{*} J_S e' = 0$ and $\dim S_0 + 2\rho = m$.

Write $\iota_X, \iota_Y \colon M_{n \times \rho}(\mathbb{A}_E) \to W(S, T)$ and $\iota_0 \colon W(S_0, T) \to W(S, T)$ for the inclusions of the three coordinates. The images of $\iota_X$ and $\iota_Y$ are isotropic and orthogonal to the image of $\iota_0$. The parabolic subgroup that fixes $X$ contains the Levi elements $m(a)$ for $a \in \mathrm{GL}_\rho(\mathbb{A}_E)$, the embedded group $\iota_0(U(S_0))$, the unipotent elements $n(b)$ for $b \in M_{\rho \times \dim S_0}(\mathbb{A}_E)$, and the central elements $n(c)$ for skew-Hermitian $c \in M_\rho(\mathbb{A}_E)$.

**Definition 7.1.3 (Mixed coordinate).** Let $\mu$ be a Haar measure on $M_{n \times \rho}(\mathbb{A}_E)$ and $\mathcal{F}$ a fundamental domain for $M_{n \times \rho}(E)$ with $\mu(\mathcal{F}) = 1$. For a theta function $f$ on $W(S, T)$ and $x \in M_{n \times \rho}(\mathbb{A}_E)$, the mixed coordinate of $f$ at $x$ is the function on $W(S_0, T)$

$$\begin{aligned} \mathcal{M} f(x)(w_0) &= \int_{\mathcal{F}} \bigl(H(\iota_Y a) H(\iota_X x) H(\iota_0 w_0) f\bigr)(0) \, d\mu(a) \\ &= \int_{\mathcal{F}} \psi\bigl(\tfrac12 \langle \iota_Y a, \iota_X x \rangle\bigr) f(\iota_Y a + \iota_X x + \iota_0 w_0) \, d\mu(a). \end{aligned}$$

The second line follows from the definition of $H$ and the orthogonality of $\iota_0$ to $\iota_X$ and $\iota_Y$. The integrand is invariant under $a \mapsto a + \alpha$ for rational $\alpha$: the quasi-periodicity of $f$ gives the factor $\psi(-\tfrac12 \langle \iota_Y \alpha, \iota_X x \rangle)$, since $Y$ is isotropic, and the phase gives the inverse factor. So $\mathcal{M} f(x)$ is a mean over the compact quotient of the $Y$ coordinate and does not depend on $\mathcal{F}$. It is the theta function form of the mixed model: a Schrödinger coordinate $x$ in the $X$ direction and a theta function in the $S_0$ direction. It is the right object because the parabolic acts on it by explicit formulas, as we now show.

**Theorem 7.1.4 (Levi factor at the origin).** Let $\omega$ be a Weil datum on $(S, T)$ and $\omega_0$ a Weil datum on $(S_0, T)$, both with characters $\chi_S, \chi_T$. Let $\mu, \mathcal{F}$ be as above and $f$ a theta function on $W(S, T)$. Then:

1. $\mathcal{M}(\omega(\iota_0 g, 1) f)(0) = \omega_0(g, 1)\, \mathcal{M} f(0)$ for every $g \in U(S_0)(\mathbb{A})$;
2. $\mathcal{M}(\omega(m(a), 1) f)(0) = \mathcal{M} f(0)$ for every $a \in \mathrm{GL}_\rho(\mathbb{A}_E)$ with $\det a = 1$;
3. $\mathcal{M}(\omega(m(a), 1) f)(0) = \chi_T(\det a)^{-1} |\det a|_E^{n/2}\, \mathcal{M} f(0)$ for every $a \in \mathrm{GL}_\rho(\mathbb{A}_E)$.

Lean: `GlobalTheory.LeviOrigin.value_at_origin` (also `GlobalTheory.T.weilRepresentation_value_at_origin_leviFactor`, a second name).

*Proof.* First, the action of the Levi factor on the mixed coordinate at the origin is scalar up to $\omega_0$. Precisely, there are continuous characters $\alpha$ of $\mathrm{GL}_\rho(\mathbb{A}_E)$ and $\xi$ of $U(S_0)(\mathbb{A})$, trivial on the rational points, such that for all $a$, $g$ and all theta functions $f$

$$\begin{aligned} \mathcal{M}\bigl(\omega(m(a) \iota_0(g), 1) f\bigr)(0) &= \alpha(a)\, \xi(g)\, |\det a|_E^{n/2}\, \omega_0(g, 1)\, \mathcal{M} f(0). \end{aligned}$$

This comes from the Heisenberg equivariance of $\omega$ and $\omega_0$ and the uniqueness of the theta distribution. Second, the local models at the split places compute both characters there: $\xi(g) = 1$ when $g$ is supported at a split place, and $\alpha(a) = \chi_T(\det a)^{-1}$ when $a - 1$ is supported at a split place. A continuous character of $U(S_0)(\mathbb{A})$ that is trivial on the rational points and on all elements supported at split places is trivial. So $\xi = 1$.

Third, a continuous character of $\mathrm{GL}_\rho(\mathbb{A}_E)$ with values in the circle is trivial on the elements of determinant $1$. So $\alpha$ factors through the determinant. If $\rho = 0$ every $a$ has determinant $1$ and $\alpha = 1 = \chi_T(\det a)^{-1}$. If $\rho \geq 1$, let $d(t)$ be the diagonal matrix with $t \in \mathbb{A}_E^{\times}$ in the first place and $1$ elsewhere. The character $t \mapsto \alpha(d(t)) \chi_T(t)$ is continuous and trivial on $E^{\times}$, so it is a Hecke character. It is trivial at the split places by the second step. A Hecke character of $E$ that is trivial at all split places is trivial. So $\alpha(d(t)) = \chi_T(t)^{-1}$. For any $a$ the matrix $a\, d(\det a)^{-1}$ has determinant $1$, so

$$\begin{aligned} \alpha(a) &= \alpha\bigl(a\, d(\det a)^{-1}\bigr)\, \alpha\bigl(d(\det a)\bigr) = \chi_T(\det a)^{-1}. \end{aligned}$$

Now put $g = 1$ in the first display: this is item 3. Put $a = 1$: since $\xi = 1$ this is item 1. If $\det a = 1$, then $\chi_T(\det a) = 1$ and $|\det a|_E = 1$, and item 3 gives item 2. $\square$

**Theorem 7.1.5 (Mixed model formulas for the source).** Let $\omega, \omega_0, \mu, \mathcal{F}$ and $f$ be as in the theorem above. Then for every $x \in M_{n \times \rho}(\mathbb{A}_E)$:

1. (target) $\mathcal{M}(\omega(1, h) f)(x) = \omega_0(1, h)\, \mathcal{M} f(h^{-1} x)$ for $h \in U(T)(\mathbb{A})$;
2. (core) $\mathcal{M}(\omega(\iota_0 g, 1) f)(x) = \omega_0(g, 1)\, \mathcal{M} f(x)$ for $g \in U(S_0)(\mathbb{A})$;
3. (Levi) $\mathcal{M}(\omega(m(a), 1) f)(x) = \chi_T(\det a)^{-1} |\det a|_E^{n/2}\, \mathcal{M} f(x a)$ for $a \in \mathrm{GL}_\rho(\mathbb{A}_E)$;
4. (unipotent) $\mathcal{M}(\omega(n(b), 1) f)(x) = H(x b)\, \mathcal{M} f(x)$, with $H$ the Heisenberg operator of $W(S_0, T)$;
5. (centre) $\mathcal{M}(\omega(n(c), 1) f)(x) = \psi\bigl(\tfrac12 \langle \iota_X x, \iota_Y(x c) \rangle\bigr)\, \mathcal{M} f(x)$.

Lean: `GlobalTheory.MixSourceFormulas.mixed_source`.

*Proof.* The Heisenberg operators preserve theta functions. From the definition, $\mathcal{M} f(x) = \mathcal{M}(H(\iota_X x) f)(0)$: the operator $H(\iota_X x)$ moves the point $x$ to the origin. By Heisenberg equivariance, $\omega(g, 1) H(\iota_X x) = H(\iota_X x')\, \omega(g, 1)$ for the point $x'$ with $\iota_X x \cdot g^{-1} = \iota_X x'$. For $g = \iota_0(g_0)$ we have $x' = x$, since $U(S_0)$ fixes $X$. For $g = m(a)$ the point $x$ moves to $x a$ in the normalisation of the formula. In both cases we reduce to the origin, where the [Theorem 7.1.4](/entry/value-at-origin/) gives the core formula and the Levi formula, applied to the theta function $H(\iota_X x) f$. The target formula is the equivariance of the mixed coordinate under $U(T)$, which acts on all three coordinates by left multiplication. The unipotent and central formulas come from the explicit action of $n(b)$ and $n(c)$ in the mixed coordinate: $n(b)$ shears the $S_0$ coordinate by $x b$, and $n(c)$ multiplies by the phase of the shear of the $Y$ coordinate. $\square$

**Remark 7.1.6 (Formalization).** The theorem on the mixed model formulas gets the reduction to the origin as the seventh component of a long conjunction ([MixedModelFormulasWittSourceProof.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/MixedModelFormulasWittSourceProof.lean#L25)); the target, unipotent and central formulas are quoted from separate lemmas, `mixedCoordinate_origin_weilRep_target_equivariant` and `wittMixedModel_unipotent_formulas`, which this section does not unfold. In the Levi theorem, the scalar form of the action, the split place values and the triviality of Hecke characters at the split places come from `weilAction_levi_origin_eq_charScalar`, `leviFactor_characters_splitPlace` and `heckeCharacter_eq_one_of_trivial_splitPlaces`. The second name is a wrapper whose proof is a `first | exact ...` tactic.
