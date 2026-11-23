---
title: The key rule for half characteristics
decls:
  - GlobalTheory.KeyTop.exists_keyRule_charHalf
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The key rule for half characteristics

This section proves the final result of the chapter: there is one rule $\kappa$ on key inputs over all fields of characteristic $0$, of weight $8N(g)$ in the theta section and $4N(g)$ in the tangent basis, that is a unit over every discrete valuation ring and that equals $1$ at the theta functions with half characteristics. The rule is built from [the key invariant](/entry/ka-st/) for the prime $2$, after a normalization, and integrality at the primes where its level is not a unit comes from the invariant for another prime. The result enters the proof at [EveryCharacter of the literature](/step/every-character-of-literature/). The background is in [Poisson summation, theta and Mellin](/learn/complex-analysis/#poisson-summation-theta-and-mellin), in [Siegel moduli schemes and level structures](/learn/abelian-varieties/#siegel-moduli-schemes-and-level-structures) and in [discrete valuation rings and lattices](/learn/commutative-algebra/#discrete-valuation-rings-and-lattices).

**Definition 2.10.1 (Key rules).** Let $N : \mathbb{N} \to \mathbb{N}$, let $g_0 \in \mathbb{N}$, and let $S(g, a, b)$ be a condition on $a, b \in \mathbb{C}^g$. A *key rule* for $(N, g_0, S)$ is a choice of a unit $\kappa(x) \in K^\times$ for every field $K$ of characteristic $0$ and every key input $x$ over $K$, with the following properties for every $x$ of dimension $g \geq g_0$.

1. *Weight.* If $x'$ is obtained from $x$ by $(a, m)$, with $a \in K$ and $m \in M_g(K)$, then $a^{8N(g)}\kappa(x') = \det(m)^{4N(g)}\kappa(x)$.
2. *Base change.* If $f : K \to K'$ is a homomorphism of fields of characteristic $0$ and $x'$ is a pullback of $x$ along $f$, then $\kappa(x') = f(\kappa(x))$.
3. *Integrality.* Let $R$ be a discrete valuation ring with fraction field $K$ of characteristic $0$, let $x$ be a key input over $R$ and let $x_K$ be a pullback of $x$ to $K$. Then there is $u \in R^\times$ with $\kappa(x_K) = u$, and $\kappa(x_k) = r(u)$ for every surjective homomorphism $r : R \to k$ onto a field of characteristic $0$ and every pullback $x_k$ of $x$ along $r$.
4. *Normalization.* If $x$ is a key input over $\mathbb{C}$, $S(g, a, b)$ holds and $x$ is normal at $(\tau, 1, a, b, 1)$, then $\kappa(x) = 1$.

Lean: `GlobalTheory.KeyPow.KeyRule`, `GlobalTheory.KeyPow.ClauseH`.

The rule is defined on all fields of characteristic $0$, not only on algebraically closed ones, and the unit of the integrality property lies in $R$ itself. Both are stronger than in a key invariant rule. The last clause of integrality concerns discrete valuation rings with a residue field of characteristic $0$; when the residue field has characteristic $p > 0$, there is no surjection onto a field of characteristic $0$ and the clause is empty.

We use two classical facts on theta functions and Siegel modular forms, as hypotheses. Write $e(w) = \exp(2\pi i w)$. The *theta inversion formula* says that for $\tau$ in the Siegel space, $a, b \in \mathbb{R}^g$ and $z \in \mathbb{C}^g$,
$$\theta\begin{bmatrix} a \\ b \end{bmatrix}(-\tau^{-1}, \tau^{-1}z)^2 = (-i)^g \det(\tau)\, e(z^{T}\tau^{-1}z)\, e(2a^{T}b)\, \theta\begin{bmatrix} b \\ -a \end{bmatrix}(\tau, z)^2.$$
The *Koecher statement* says that for $g \geq 2$ a function that is holomorphic on the Siegel space and invariant under $\mathrm{Sp}_{2g}(\mathbb{Z})$ is constant on the Siegel space. We also use the uniformization theorem, the algebraicity of tori and the laws, as in [the key invariant theorem](/entry/ka-st/).

Two facts from the development are used with their statements. First, the laws imply descent to countable fields, the hypothesis of the key invariant theorem. Second, the *normalization theorem*: assume the laws, the uniformization theorem, the theta inversion formula, the Koecher statement and the algebraicity of tori; let $g \geq 1$, and let $\kappa_{2g}$ be a key invariant rule of dimension $2g$, weight $c$ and level $M$. Then there is a choice $\kappa(x) \in K^\times$ for key inputs over all fields $K$ of characteristic $0$ such that, for $x$ of dimension $g$, the weight law holds with $2c$ in place of $c$, base change holds for all fields of characteristic $0$, the integrality of a key rule holds over discrete valuation rings in which $M$ is a unit, and $\kappa$ has the *normal value*
$$\kappa(x) = \bigl(\det(m)^4 / c_0^{8}\bigr)^{2c}$$
for every $x$ over $\mathbb{C}$ that is normal at $(\tau, m, a, b, c_0)$, with $(a, b)$ a half characteristic, $c_0 \neq 0$ and $\det m \neq 0$. The normal value is the one that the weight law forces from the value $1$ at $(\tau, 1, a, b, 1)$. The rule in dimension $g$ is made from the rule in dimension $2g$ by applying it to the square $x \times x$.

**Lemma 2.10.2 (Comparison of normalized rules).** Assume the uniformization theorem and descent to countable fields. Let $\kappa$ and $\kappa'$ be as in the conclusion of the normalization theorem for dimension $g$, with exponents $n$ and $n'$ in place of $2c$ in the normal value. Then $\kappa(x)^{n'} = \kappa'(x)^{n}$ for every key input $x$ of dimension $g$ over a field $K$ of characteristic $0$.

Lean: `GlobalTheory.KeyHouse.pow_eq_pow`.

*Proof.* By descent, $x$ is a pullback of a key input $x_0$ over a countable subfield $K_0 \subseteq K$. There is a field homomorphism $\sigma : K_0 \to \mathbb{C}$: the algebraic closure $\Omega$ of $K_0(X_t : t \in \mathbb{R})$ is algebraically closed of characteristic $0$ and of cardinality $2^{\aleph_0}$, so $\Omega \cong \mathbb{C}$ by Steinitz's theorem. Let $y$ be a pullback of $x_0$ along $\sigma$. By the uniformization theorem, $y$ is normal at some $(\tau, m, a, b, c_0)$ with $(a, b)$ a half characteristic, $c_0 \neq 0$ and $\det m \neq 0$. Then
$$\kappa(y)^{n'} = \bigl(\det(m)^4/c_0^8\bigr)^{n n'} = \kappa'(y)^{n}.$$
By base change $\kappa(y) = \sigma(\kappa(x_0))$ and $\kappa'(y) = \sigma(\kappa'(x_0))$, so $\kappa(x_0)^{n'} = \kappa'(x_0)^n$ since $\sigma$ is injective. Base change along $K_0 \to K$ gives the claim for $x$. $\square$

**Lemma 2.10.3 (Units from powers).** Let $R$ be a discrete valuation ring with fraction field $K$, let $z \in K$, $n \geq 1$ and $u \in R^\times$ with $z^n = u$. Then $z \in R^\times$.

Lean: `GlobalTheory.KeyHouse.exists_unit_of_pow`.

*Proof.* The element $z$ is a root of $X^n - u \in R[X]$, so it is integral over $R$. Since $R$ is integrally closed, $z \in R$. Then $z \cdot z^{n-1}u^{-1} = 1$, so $z$ is a unit. $\square$

**Lemma 2.10.4 (Primes at a non-unit).** Let $R$ be a local ring and $M \geq 1$ an integer that is not a unit in $R$. Then the residue field of $R$ has prime characteristic $p$, and every integer prime to $p$ is a unit in $R$. If $R$ admits a surjection onto a field of characteristic $0$, every integer $M \geq 1$ is a unit in $R$.

Lean: `GlobalTheory.KeyHouse.exists_prime_of_not_isUnit`, `GlobalTheory.KeyHouse.isUnit_of_surjective`.

*Proof.* An integer is a unit in $R$ if and only if its image in the residue field $k$ is nonzero. Since $M$ maps to $0$ in $k$, the characteristic of $k$ is a prime $p$, and an integer prime to $p$ maps to a nonzero element. A surjection $r : R \to k'$ onto a field has kernel the maximal ideal, so $k' \cong k$; if $k'$ has characteristic $0$, every $M \geq 1$ maps to a nonzero element. $\square$

**Theorem 2.10.5 (The key rule for half characteristics).** Assume the laws, the uniformization theorem, the theta inversion formula, the Koecher statement and the algebraicity of tori. Then there is $N : \mathbb{N} \to \mathbb{N}$ with $N(g) \geq 1$ for all $g$ such that a key rule for $(N, 1, S)$ exists, where $S(g, a, b)$ says that $(a, b)$ is a half characteristic.

Lean: `GlobalTheory.KeyTop.exists_keyRule_charHalf`.

*Proof.* The laws give descent to countable fields, and then the key invariant theorem gives, for every $g \geq 1$ and prime $p$, a key invariant rule of dimension $2g$, weight $c$ and level $M$ with $p \nmid M$. The normalization theorem turns it into a rule $\kappa_{g, p}$ in dimension $g$ with exponent $2c$ and level $M_{g, p} = M$. Put $N(g) = 2c$ for the prime $p = 2$, with $N(0) = 1$, and let $\kappa(x) = \kappa_{g, 2}(x)$ for $x$ of dimension $g$.

The weight law and base change are those of $\kappa_{g, 2}$. For the normalization, let $x$ be normal at $(\tau, 1, a, b, 1)$ with $(a, b)$ a half characteristic. The normal value gives $\kappa(x) = (1^4/1^8)^{N(g)} = 1$.

For integrality, let $R$, $x$ and $x_K$ be as in the property. If $M_{g, 2}$ is a unit in $R$, the integrality of $\kappa_{g, 2}$ gives the claim. Otherwise, by the lemma on primes, the residue field of $R$ has prime characteristic $p$, and every integer prime to $p$ is a unit in $R$. Take the rule $\kappa' = \kappa_{g, p}$, with exponent $n'$ and level $M_{g, p}$ prime to $p$, hence a unit in $R$. Its integrality gives $u' \in R^\times$ with $\kappa'(x_K) = u'$. By the comparison of normalized rules,
$$\kappa(x_K)^{n'} = \kappa'(x_K)^{N(g)} = u'^{N(g)} \in R^\times,$$
and by the lemma on units from powers $\kappa(x_K) = w$ for some $w \in R^\times$. The second clause of integrality is empty here: a surjection of $R$ onto a field of characteristic $0$ would make $M_{g, 2}$ a unit in $R$, by the lemma on primes. $\square$

**Remark 2.10.6.** The comparison of rules for two primes is what removes the level. Each key invariant rule is integral only where its level $M$ is a unit, and $M$ can be chosen prime to any one prime, but not to all primes at once. Normalized rules for two primes agree up to powers, so a unit for one of them gives a unit for the other, by integral closure. The value $1$ at half characteristics is what makes the comparison possible: it fixes each rule at the normal inputs, with no constant left, so the two rules agree up to powers.

**Remark 2.10.7 (Formalization).** The theorem is in [ExistsKeyRuleCharHalf.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/ExistsKeyRuleCharHalf.lean#L28). Its proof passes the hypotheses to `T.thetaKeyRule_exists_of_algebraic_invariants`, a second name of `KeyHouse.keyRule_of_kaSt` ([ThetaKeyRuleExistsOfAlgebraicInvariants.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/ThetaKeyRuleExistsOfAlgebraicInvariants.lean#L95)), which is the proof above. Descent is `T.keyData_descend_countable_subrings`, the normalization theorem is `T.exists_normalised_key_invariant_rule_char_zero`, and the normal key inputs over $\mathbb{C}$ come from `KeyNormalExists.exists_normalAt`; we used their statements. The rule for dimension $g$ calls the key invariant statement at dimension $2g$ (line 101), and the normalization applies it to the square $x \times x$ (`exists_rule_sq` in ExistsNormalisedKeyInvariantRuleCharZero.lean, line 48). The definitions are in [KeyRuleOneOfKeyFormula.lean](lean:Development/AbelianVarietyTheory/Definitions/KeyFormula/KeyRuleOneOfKeyFormula.lean#L41). The hypotheses are `ThetaUnifAV`, `Key.Chi.InversionStatement`, `Key.PhHoloStatement` and `TorusAlgebraic`.

## Notes and references

The chapter feeds into [EveryCharacter of the literature](/step/every-character-of-literature/) through the key rule, and into [the published results](/entry/real-metaplectic-representation-of-literature/), [Zarhin's trick](/entry/zarhin/) and [the packing statement](/entry/packing/) of later volumes through the first three sections.

The metaplectic representation is due to Weil; the form used here, with the Schwartz space and the derived action, follows Folland. Zarhin's trick is the statement that $(A \times A^\vee)^4$ is principally polarized; the Lean form is a retract of a principally polarized abelian scheme over a valuation ring, and it does not name the polarization. The theorem of the cube and the complex uniformization are in Mumford. The key invariant is an algebraic form of the key formula (formule clé) of Moret-Bailly, which compares the eighth power of the determinant of $\pi_*L$ with a power of the Hodge bundle; here it is built from the torsion of Koszul complexes of theta sections, not from a moduli argument, and its integrality is proved one discrete valuation ring at a time. The theta inversion formula and the Koecher principle are classical; they enter as hypotheses.

- G. B. Folland, *Harmonic Analysis in Phase Space*, Annals of Math. Studies 122, Chapter 4.
- D. Mumford, *Abelian Varieties*, §1 to §3 and §6.
- D. Mumford, *Tata Lectures on Theta I*, Chapter II.
- H. Matsumura, *Commutative Ring Theory*, §16.
