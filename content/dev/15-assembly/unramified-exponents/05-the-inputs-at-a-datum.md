---
title: The inputs at a datum
decls:
  - GlobalTheory.T.exists_inputs_of_galHodgeN_roots
  - GlobalTheory.TwInputs.exists_inputs_of_hkSup_galHodge
  - GlobalTheory.TwGalInputs.galois_inputs_alt
  - GlobalTheory.TripleLocal.adm1_adm8_selfDual_noJump_of_isTriple
  - GlobalTheory.TripleGal.adm1_adm8_selfDual_noJump_of_tripleAttN
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The inputs at a datum

This section builds the record of inputs at one datum $D$: an integer function $N_0$ and twenty-one facts on the theta series and the Galois representations of $D$. Step 1 of [the local export theorem](/entry/export-at-of-bundles-alt/) of Section 4 uses this record, and the twist theorem for all powers consumes twenty of its facts. Eight facts come from the Galois side: they are the Galois conditions at the twist indices with a nonzero index place, and the main work here is to get them from an attached Galois triple. The other facts come from the series side and from the Hecke operators.

Let $D$ be a datum, with coefficient field $L_0$ and twist indices $i$. For each twist index $i$ there is a prime $\ell_i$, a discrete valuation ring $O_i$ over $\mathbb{Z}_{\ell_i}$, and for each sign $s$ of $i$ a Galois representation $T_{i,s}$ of the Galois group of the CM field $E$ of $D$, with values in $\mathrm{GL}_r(O_i)$. Let $t$ be the weight of $D$ and $\varepsilon_i$ the cyclotomic character at $i$ with values in $O_i^\times$.

**Definition 6.5.1 (Galois conditions).** Fix a twist index $i$ with a nonzero index place and a sign $s$.

1. $T_{i,s}$ is *self-dual* if there is $A \in \mathrm{GL}_r(O_i)$ such that for all $g, g'$ in the Galois group with $g' = c\, g\, c^{-1}$ for complex conjugation $c$,

$$T^\vee_{i,s}(g') = A\, \bigl(\varepsilon_i(g)^t\, T_{i,s}(g)\bigr)\, A^{-1}.$$

2. $T_{i,s}$ has *no jump* if, at each place $v$ of $E$ above $\ell_i$ and each embedding $\tau$, every Hodge-Tate jump $a$ of the representation at $v$ satisfies $a < -1$ or $a > t$.
3. *Condition* $\mathrm{adm}_1$ holds if at each such $(i, s)$ the coefficient ring has the isotypic valuation property: the valuation of polynomials in the letters of the ring is additive on products and satisfies the ultrametric inequality on sums, with the further clauses of that property.
4. *Condition* $\mathrm{adm}_2$ holds if at each such $(i, s)$ the coefficient ring has valuation stability: coordinate multiplication and enlarging letters.
5. *Condition* $\mathrm{adm}_8$ holds if at each such $(i, s)$ there is a character twist of $T_{i,s}$ for the exponent data of $D$.
6. *Conditions* $\mathrm{adm}_9(N_0)$ and $\mathrm{adm}_{10}$ are integrality statements for the theta class values: $\ell_i^{N_0(i)}$ times each class value is integral, and the values at two conjugate places of a set $Q$ are related through a Frobenius.
7. The *set hypothesis* at $i$ is the conjunction of seven conditions: a trivial condition; self-duality and no jump for every good sign; nonvanishing of the sum of class values; existence of a good integer for each class; $r \ge 100$; and $g_k \ge 2r$ for each $k$.

A *Galois triple* for $D$ assigns to each twist index and sign a Galois representation attached to the automorphic data of $D$; an *attached* triple adds, at each $(i, s)$, the unramified, Hodge and Frobenius properties of the attachment. A Galois side $G$ of $D$ carries a tie between the Weil-Deligne data and the automorphic data, a Galois triple, a character side, a lambda datum with its tie, the rank bound $r \ge 100$ and the bounds $g_k \ge 2r$. The *Hodge condition* for $D$ and a tie says that, for each prime $\ell$, each isomorphism $\iota : \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$ and each conjugate self-dual regular algebraic cuspidal representation $\pi$, there is an attached Galois representation which is de Rham above $\ell$, crystalline where $\pi$ is unramified, and potentially crystalline; together with a wild inertia condition, a separation condition and tameness for characters. See [crystalline and de Rham representations](/learn/galois-representations/#crystalline-de-rham-and-potentially-semistable-representations).

**Lemma 6.5.2 (Galois conditions from an attached triple).** Let $D$ be a datum and $P$ a Bloch-Kato frame of $D$. Assume that the Frobenius elements of split places are dense, that each twist index with a nonzero index place has a local tie at $\ell_i$, condition $\mathrm{adm}_2$, and that $P$ carries an attached triple at each $(i, s)$ with $i$ of nonzero index place. Then $\mathrm{adm}_1$ holds for $P$, $\mathrm{adm}_8$ holds for $D$, and for each $i$ with a nonzero index place and each sign $s$, $T_{i,s}$ is self-dual and has no jump for $P$.

Lean: `GlobalTheory.TripleGal.adm1_adm8_selfDual_noJump_of_tripleAttN`.

*Proof.* Fix $(i, s)$. The attached triple gives an embedding $\iota$ and a multiset $J$ of Hodge-Tate weights with good jumps, and the Hodge type at $(i, s)$. The good jumps give the absence of a jump in $(-1, t]$: this is the no jump condition. For $\mathrm{adm}_1$, the triple gives an unramified representation with its Hodge type; the representation has no invariants at the places above $\ell_i$, by the local tie, $\mathrm{adm}_2$, the triple and the no jump condition; and the count of negative jumps of the conjugate is the right one by the good jumps. These three facts give the isotypic valuation property. For $\mathrm{adm}_8$, the unramified representation and the Frobenius traces of the Hecke operators give a character twist. For self-duality, the Frobenius duality of the triple and the density of split Frobenius elements give that the characteristic polynomials of $T^\vee_{i,s}(c g c^{-1})$ and $\varepsilon_i(g)^t T_{i,s}(g)$ agree; with $\mathrm{adm}_2$ this gives a self-dual lattice and the matrix $A$. $\square$

**Lemma 6.5.3 (Galois conditions from a Galois triple).** Let $D$ be a datum with a tie $T$ and a character side. Assume that the Frobenius elements of split places are dense, the Hodge condition for $D$ and $T$, condition $\mathrm{adm}_2$, and that $D$ has a Galois triple. Then, for the standard frame of $D$, $\mathrm{adm}_1$ and $\mathrm{adm}_8$ hold, and for each $i$ with a nonzero index place, a trivial condition holds and each $T_{i,s}$ is self-dual and has no jump.

Lean: `GlobalTheory.TripleLocal.adm1_adm8_selfDual_noJump_of_isTriple`.

*Proof.* A Galois triple, with the character side, the density of Frobenius elements and the Hodge condition, gives an attached triple at each $(i, s)$. The local ties at $\ell_i$ are part of the datum $D$. The lemma above applies. $\square$

**Theorem 6.5.4 (Galois inputs).** Assume Chebotarev for primes of degree one, global Artin reciprocity and the toric denominator bound. Let $D$ be a datum and $G$ a Galois side of $D$ with the Hodge condition for $D$ and the tie of $G$. Then:

1. $\mathrm{adm}_1$, $\mathrm{adm}_2$ and $\mathrm{adm}_8$ hold;
2. the exponent data of $D$ are good, and the sign condition holds at all indices;
3. there is $N_0$ with $\mathrm{adm}_9(N_0)$, and $\mathrm{adm}_{10}$ holds;
4. the set hypothesis holds at each twist index with a nonzero index place.

Lean: `GlobalTheory.TwGalInputs.galois_inputs_alt`.

*Proof.* The label of $G$ is of full degree, so wild inertia acts trivially; with the triple of $G$ this gives $\mathrm{adm}_2$. Chebotarev for primes of degree one gives the density of split Frobenius elements. The lemma on Galois triples gives $\mathrm{adm}_1$ and $\mathrm{adm}_8$. The triple gives the goodness of the exponent data and the sign condition. The lambda datum of $G$ with its tie gives a toric element; global Artin reciprocity and the toric bound then give $N_0$ with $\mathrm{adm}_9(N_0)$, and $\mathrm{adm}_{10}$. The set hypothesis follows from Chebotarev, the tie, the character side, the Hodge condition, $\mathrm{adm}_2$, the triple, the lambda datum and the bounds of $G$. $\square$

**Theorem 6.5.5 (Inputs at a datum).** Assume Chebotarev for primes of degree one, global Artin reciprocity and the toric denominator bound. Let $D$ be a datum, $X$ a real side, $E$ Hecke form data of $D$, $Y$ a series side over $X$ for $E$, and $G$ a Galois side. Assume the rationality rows at each index with a nonzero index place, the coefficient bound, the preservation of the sup lattice by Hecke operators at each $j$, the Hodge condition for $D$ and the tie of $G$, and that every $z \in \mathbb{C}$ with $z^{g_k (g_k - 1)} = 1$ lies in the image of $L_0$. Then there is $N_0$ such that the record of inputs at $(D, E, N_0)$ holds.

Lean: `GlobalTheory.TwInputs.exists_inputs_of_hkSup_galHodge` (also `GlobalTheory.T.exists_inputs_of_galHodgeN_roots`, a second name).

*Proof.* We fill the fields of the record.

1. Galois side: the theorem on Galois inputs gives $\mathrm{adm}_1$, $\mathrm{adm}_2$, $\mathrm{adm}_8$, the goodness and sign conditions, $N_0$ with $\mathrm{adm}_9$, $\mathrm{adm}_{10}$ and the set hypothesis.
2. Laws: the rationality rows give the laws of the series side, and with them the type of the coefficients.
3. Hecke operators: the preservation of the sup lattice gives the sup laws, the full sup condition, the Hecke condition and two commutation facts, and also the semisimplicity of the Hecke action.
4. Series: the laws give the relation, the third law and the type; the roots of unity give the fourth admissibility fact; the coefficient bound gives the universal sup; the universal character and the offset come from $Y$.

All hypotheses are used. $\square$

**Remark 6.5.6 (Formalization).** The theorems are at [InputsOfSidesStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/InputsOfSidesStatement.lean#L15), [InputsOfSides.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/InputsOfSides.lean#L15), [GaloisInputs.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GaloisInputs.lean#L19), [GaloisHypothesesOfIsTriple.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GaloisHypothesesOfIsTriple.lean#L35) and [GaloisHypothesesOfAttached.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GaloisHypothesesOfAttached.lean#L23). The two lemmas on Galois conditions conclude a conjunct `True` at each index (line 28 of the second file proves it by `trivial`); it matches the first conjunct of `SetHyp`, which is also `True` ([BlochKatoPhases.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/BlochKatoPhases.lean#L327)). In `adm1_adm8_selfDual_noJump_of_isTriple` the local tie hypothesis is discharged by `fun _ _ => ⟨_, ⟨D.locT _⟩⟩`, so it is a field of the datum. The file declares the sections `Twist`, `Chars` and `Triple` with variables and no declarations in them. The two names of the inputs theorem name different hypotheses (`HkSupAt` and `GalHodgeN`, or `GalHodgeN` and the roots), though both take all of them; the second name is proved by a `first | exact … | …` tactic. The definitions of `IsotypicValuationAtRing` and `ValuationStabilityAtRing` are at [Lemma5aAt.lean](lean:Formalism/SharpRestriction/GrowthBounds/Lemma5aAt.lean#L27); we have stated only their first clauses. We did not unfold `TripleAttN`, `IsGaloisTriple`, `characterTwistExists`, `SOk`, `QOk`, the fields of `Inputs` or the laws, so the descriptions of the attached triple and of steps 2 to 4 of the last proof follow the names of the lemmas.
