---
title: The dictionary of moved jets
decls:
  - GlobalTheory.DictFree.twisted_dictionary_eventually_large
  - GlobalTheory.T.translated_jets_dictionary
  - GlobalTheory.MovedDict.jets_moved_by_translation
  - GlobalTheory.T.twist_moved_vacuum_correspondence
  - GlobalTheory.MovedDict.moved_vacuum_vector_correspondence
  - GlobalTheory.T.twisted_moved_vacuum_kappa
  - GlobalTheory.MovedDict.moved_vacuum_kappa_eval
  - GlobalTheory.T.movedKappa_rational_of_arithmetic
  - GlobalTheory.MovedKappaArith.movedKappa_arithmetic
  - GlobalTheory.T.exists_unique_moved_kappa_jet
  - GlobalTheory.MovedKappaEx.exists_moved_kappa
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The dictionary of moved jets

The size bounds of [Section 3.12.2](/entry/sum-size-finite-away-archimedean-combined/) and the rationality of sums need to know the jets of the vacuum vector after it is moved by finite points and by Heisenberg translates. This section proves a dictionary: the jets of a moved vector are a fixed constant times an algebraic combination of jets of one entire function, the intertwining operator of two self-dual lattices, with coefficients that are small at every embedding and integral up to a power of the level. The dictionary is one of the hypotheses checked in the step [the hypotheses are not empty](/step/nonempty-hyps/). The heart of the proof is a constant $\kappa$ that relates the jets of the moved vacuum to the jets of the intertwining operator; we prove that it exists, that it is unique, and that it is a unit at the good primes.

We keep the notation of Sections 6 and 12. Fix a choice of the row with grid $G$ and Weil datum $W$, and let $p$ be a definite pair of the grid, with a small node and a big node. Let $x$ and $y$ be finite points at the small and at the big node. At each prime $q$ the grid gives lattices $L_q(x)$ and $L_q(y)$; we say that $q$ is good for $(x, y)$ if both are the standard lattice at $q$.

**Definition 3.19.1 (Moved data).** Let $L_s$ and $L_t$ be lattices in the two spaces of the pair. Let $\Lambda(L_s, L_t)$ be the lattice of the Heisenberg group that they define, and let $I(z)$ be the intertwining operator between the standard lattice model and the model of $\Lambda(L_s, L_t)$, as a function of a complex vector $z$ of the space of the pair, evaluated at the base exponent of $p$. For a vector $s$ let $U(s)$ be the translate by $s$. For a monomial $m$ in the variables of the pair let $\partial^m f(0)$ be the value at $0$ of the differential operator of $m$ applied to a function $f$, and let $\pi(m) = \prod_v \omega_v^{m_v}$ be the product of the periods of the variables. The jet of a vector $\phi$ at $m$ is the coefficient of $m$ in its Fock expansion.

**Definition 3.19.2 (Mod one).** A complex number $\kappa$ is of modulus one everywhere if $\kappa$ is algebraic and $|\sigma(\kappa)| = 1$ for every embedding $\sigma : \overline{\mathbb Q} \to \mathbb C$.

**Definition 3.19.3 (Dictionary).** A choice satisfies the dictionary if the following holds for every index $t$, every definite pair $p$, every integer $k > 0$, every coset datum $d$ of level $k$ at $t$ and $p$ with trivial twist and with the local places of $t$, and all finite points $x$, $y$. There are self-dual lattices $L_s$, $L_t$, a number $\kappa$ of modulus one everywhere, algebraic numbers $r_1, \dots, r_n$ and vectors $s_1, \dots, s_n$ with:

1. $k\, s_i \in \Lambda(L_s, L_t)$ for every $i$;
2. $k^{f a b}\, r_i$ is an algebraic integer for every $i$, where $f$ is the degree of the datum and $a$, $b$ are the ranks of the two spaces of the pair;
3. $\sum_i |\rho(r_i)| \le 1$ for every embedding $\rho : \overline{\mathbb Q} \to \mathbb C$;
4. at every prime $q$ that is good for $(x, y)$, $L_s$ and $L_t$ are standard at $q$, and $|\lambda(\kappa)| = 1$ for every embedding $\lambda : \overline{\mathbb Q} \to \mathbb C_q$;
5. for every monomial $m$, the jet of the vector of $d$ moved by $(x, y)$ at $m$ is

$$c_0(p)\, \mathrm{opp}_p\Bigl(\pi(m)\, \partial^m\Bigl(\kappa \sum_i r_i\, U(s_i)\, I\Bigr)(0)\Bigr).$$

Here $c_0(p)$ is a constant of the pair and $\mathrm{opp}_p$ is an involution of $\mathbb C$ attached to the orientation of $p$.

Condition 3 says that the coefficients are small at every embedding, and condition 2 that their denominators divide a power of the level. With condition 4 these are exactly the facts that the size bounds need at the archimedean places, at the primes of the level and at the good primes.

We work up from the vacuum. Let $\phi_0$ be the vacuum vector of the pair, and for finite points $x$, $y$ let $\phi_{x,y}$ be the vacuum moved by $(x u, y u)$, where $u$ are the fixed points of the grid frames.

**Theorem 3.19.4 (A moved constant exists and is unique).** Let $L_s$, $L_t$ be the self-dual lattices of the moved vacuum $\phi_{x,y}$. There is a number $\kappa$ of modulus one everywhere such that the jets of $\phi_{x,y}$ are

$$c_0(p)\, \mathrm{opp}_p\bigl(\pi(m)\, \partial^m(\kappa I)(0)\bigr)$$

for every monomial $m$, and $|\lambda(\kappa)| = 1$ for every embedding $\lambda$ into $\mathbb C_q$ at every good prime $q$. Any $\kappa$ with this jet identity is unique.

Lean: `GlobalTheory.MovedKappaEx.exists_moved_kappa` (also `GlobalTheory.T.exists_unique_moved_kappa_jet`, a second name).

*Proof.* Uniqueness first. The operator $I$ is entire and not $0$, so it has a nonzero Taylor coefficient. The periods and the factorials are not $0$. So the jet identity at that monomial fixes $\kappa$.

For existence we prove a stronger claim for every finite set $Q$ of good primes: there is $\kappa$ of modulus one everywhere with the jet identity and with $|\lambda(\kappa)| = 1$ at the primes of $Q$. Decompose $x = r s x_0$ and $y = r' s' y_0$, where $x_0$, $y_0$ are base points, $s$, $s'$ lie in subgroups that split off, and $r$, $r'$ are rational points. At $(x_0, y_0)$ the moved vacuum has an algebraic root: a $\kappa_0$ of modulus one everywhere with the jet identity. Now move along the generators of the split-off subgroups. Each generator multiplies the constant by a number $c$ of modulus one everywhere that is a unit at the primes off a finite set, which we can take to avoid $Q$. By induction on the closure of the generators we reach $(s x_0, s' y_0)$. The last move by the rational points $r$, $r'$ changes the jets by a rational move with the same properties. This gives the claim.

Take $Q = \emptyset$ for the constant $\kappa$. For a good prime $q$, take $Q = \{q\}$: the claim gives a constant that is a unit at $q$, and by uniqueness it is $\kappa$. $\square$

**Theorem 3.19.5 (Arithmetic of the moved constant).** Every $\kappa$ with the jet identity of the previous theorem is of modulus one everywhere, and $|\lambda(\kappa)| = 1$ for every embedding into $\mathbb C_q$ at every good prime $q$.

Lean: `GlobalTheory.MovedKappaArith.movedKappa_arithmetic` (also `GlobalTheory.T.movedKappa_rational_of_arithmetic`, a second name).

*Proof.* By [Theorem 3.19.4](/entry/exists-moved-kappa/) there is a constant $\kappa_0$ with the jet identity and with both properties. By the uniqueness in the same theorem, $\kappa = \kappa_0$. $\square$

**Theorem 3.19.6 (Evaluation of the moved constant).** There are self-dual lattices $L_s$, $L_t$ and a number $\kappa$ with the jet identity for $\phi_{x,y}$, of modulus one everywhere and a unit at every good prime.

Lean: `GlobalTheory.MovedDict.moved_vacuum_kappa_eval` (also `GlobalTheory.T.twisted_moved_vacuum_kappa`, a second name).

*Proof.* The jets of the moved vacuum span the line of the jets of $I$; this gives $\kappa$ with the jet identity. Its arithmetic is [Theorem 3.19.5](/entry/moved-kappa-arithmetic/). $\square$

**Theorem 3.19.7 (Moved vacuum vectors).** At large scale, for every choice of the row, every definite pair $p$ and all finite points $x$, $y$, there are self-dual lattices $L_s$, $L_t$ and a number $\kappa$ of modulus one everywhere with these properties: the operator $I$ is entire; at every good prime $q$ the lattices are standard and $\kappa$ is a unit; $\phi_{x,y}$ is a vacuum vector for the moved lattices; the moved lattice acts on $\phi_{x,y}$ through the Heisenberg action; and the jets of $\phi_{x,y}$ are given by the jet identity.

Lean: `GlobalTheory.MovedDict.moved_vacuum_vector_correspondence` (also `GlobalTheory.T.twist_moved_vacuum_correspondence`, a second name).

*Proof.* The decomposition of the twisted moved series gives $L_s$, $L_t$ and the vacuum property of $\phi_{x,y}$ for the moved lattices. [Theorem 3.19.6](/entry/moved-vacuum-kappa-eval/) gives $\kappa$ and its arithmetic. The remaining properties come from three lemmas on the moved lattices: the intertwining operator is entire, the vacuum integral gives the equality of lattices at the good primes, and the moved lattice acts on a vacuum vector of its model. $\square$

**Theorem 3.19.8 (Jets moved by translation).** At large scale the following holds for every choice, every definite pair $p$ and all finite points $x$, $y$. Take $L_s$, $L_t$ and $\kappa$ as in the previous theorem. For every Heisenberg translate $w$ with $k w \in \Lambda(L_s, L_t)$, there are a root of unity $\zeta$ and a vector $s$ with $k s \in \Lambda(L_s, L_t)$ such that the jets of the translate of $\phi_{x,y}$ by $w$ are

$$c_0(p)\, \mathrm{opp}_p\bigl(\pi(m)\, \partial^m(\kappa\, \zeta\, U(s)\, I)(0)\bigr).$$

Lean: `GlobalTheory.MovedDict.jets_moved_by_translation` (also `GlobalTheory.T.translated_jets_dictionary`, a second name).

*Proof.* Take the data of [Theorem 3.19.7](/entry/moved-vacuum-vector-correspondence/). A finite Heisenberg translate of a self-dual vacuum is, up to a root of unity, the translate $U(s)$ of the vacuum with $k s$ in the lattice; this is the formula for the Fock jets of a translated self-dual vacuum. Insert it into the jet identity for $\phi_{x,y}$. $\square$

**Theorem 3.19.9 (The dictionary).** Assume the local inputs and $\mathrm{Inp}(D)$ for every datum $D$. Then the dictionary holds at large scale.

Lean: `GlobalTheory.DictFree.twisted_dictionary_eventually_large`.

*Proof.* Let $d$ be a coset datum of level $k$. Its vector is a finite combination $\sum_i c_i\, w_i \cdot \phi_{x,y}$ of Heisenberg translates of the moved vacuum, with $k w_i$ in the lattice and coefficients $c_i$ with $\sum_i |\rho(c_i)| \le 1$ and $k^{fab} c_i$ integral. By [Theorem 3.19.8](/entry/jets-moved-by-translation/) each translate gives a root of unity $\zeta_i$ and a vector $s_i$. Put $r_i = \mathrm{opp}_p(c_i)\, \zeta_i$. Then $|\rho(\zeta_i)| = 1$, so the bound on $\sum_i |\rho(r_i)|$ and the integrality carry over from the $c_i$, and the jets of $d$ are given by condition 5 by linearity. Conditions 1 and 4 come from the previous theorems. $\square$

**Remark 3.19.10 (Formalization).** The moved vacuum theorem ([MovedVacuumVectorCorrespondence.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/MovedVacuumVectorCorrespondence.lean#L24)) has all thresholds $0$ and does not use the conditions of the scale. The route to the arithmetic of $\kappa$ is roundabout: the evaluation ([TwistedMovedVacuumKappa.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedMovedVacuumKappa.lean#L21)) gets $\kappa$ from the span of the jets and its arithmetic through uniqueness ([MovedKappaRationalOfArithmetic.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/MovedKappaRationalOfArithmetic.lean#L53)), although the existence theorem already gives both at once. The uniqueness of $\kappa$ is proved twice, at line 24 of that file and in [ExistsUniqueMovedKappaJet.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ExistsUniqueMovedKappaJet.lean#L26). The second name of the arithmetic speaks of rationality, but the statement is about modulus one and units. The file of the dictionary has a further wrapper at line 83 ([TwistedDictionaryEventuallyLarge.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedDictionaryEventuallyLarge.lean#L83)). The statement of the dictionary is defined in [DictAt.lean](lean:Development/AbelianVarietyTheory/Statements/PlaceShiftStatements/DictAt.lean#L21). We have not unfolded the coset data, the involution $\mathrm{opp}_p$, the intertwining operator, the decomposition of points, the algebraic root at the base points or the rational move.
