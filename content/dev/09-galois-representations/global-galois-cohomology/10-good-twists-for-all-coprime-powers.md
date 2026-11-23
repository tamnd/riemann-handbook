---
title: Good twists for all coprime powers
decls:
  - GlobalTheory.TwistChoiceAll.admissibleIndexBoundAllPowers_of_conditions
  - GlobalTheory.TwExportSup.twistTheorem_allPowers_of_selmer_supLattice
  - GlobalTheory.TwExportTop.twistAllPowers_of_galoisCohomology_classField
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Good twists for all coprime powers

This section constructs, at each twist index $i$, a finite set $Q$ of auxiliary [places](/learn/number-fields/#places-and-completions) and a ray class character $\psi'$ ramified exactly at $Q$, such that every power $\psi'^a$ with $a$ prime to $\ell_i$ is a good twist. A good twist has small [Selmer group](/learn/galois-cohomology/#selmer-and-tate-shafarevich-groups) lengths, nonzero theta values of controlled valuation, and small tame valuations at the places of $Q$. The inputs are the order bounds and the Selmer presentation of the previous section, the Euler characteristic and duality statements of the local and global theory, and [class field theory](/learn/class-field-theory/#global-class-field-theory) for ray class characters. The result is used by [the local export condition from rational rows](/entry/export-at-of-bundles-alt/).

### Twists and their bounds

Fix a datum $D$ with its twist indices. At an index $i$ there are a prime $\ell = \ell_i$, an integer $\nu = \nu_i \geq 0$, a discrete valuation ring $O$ over $\mathbb{Z}_\ell$, and for each $k \geq 1$ an extension $O_k$ of $O$ that contains a fixed primitive $\ell^k$-th root of unity $\zeta_k$. Write $v$ for the valuation on $O_k$ normalized by $v(\ell) = 1$. For a finite set $Q$ of places of the CM field $E$, let $\mathrm{RCG}(Q)$ be the ray class group of conductor supported on $Q$, and let $\mathrm{art}_Q$ be the [Artin map](/learn/class-field-theory/#global-class-field-theory) from the Galois group to it.

**Definition 2.10.1 (admissible twist).** A homomorphism $\psi' : \mathrm{RCG}(Q) \to O_k^\times$ is admissible for a finite set $A$ of places if every place of $Q$ is split over the totally real subfield, of degree one and unramified over $\mathbb{Q}$; $Q$ avoids $A$ and the bad places $S_0$; the character $\psi = \psi' \circ \mathrm{art}_Q$ has open kernel, satisfies $\psi(c g c^{-1}) = \psi(g)^{-1}$ for complex conjugation $c$, and takes values in $\langle \zeta_k \rangle$; $\psi$ is ramified exactly at $Q$; and $\psi$ is trivial on the [decomposition groups](/learn/galois-representations/#decomposition-groups-inertia-and-frobenius) above $\ell$.

For $\varepsilon' > 0$, the twist $\psi'$ has bounds within $\varepsilon'$ if four conditions hold.

1. Selmer lengths: there are numbers $\varepsilon_T(s) \geq 0$ with $\sum_s \varepsilon_T(s) \leq \varepsilon'$, such that for every good sign $s$ the Selmer length of the twist of the $s$-part by $\psi$ is at most $\nu + \varepsilon_T(s)$.
2. Theta values: for every $\lambda$ in the group ring basis, the theta value $\theta_\lambda(\psi)$ is nonzero and $-N_0(i) \leq v(\theta_\lambda(\psi)) \leq c_0(\lambda) + \varepsilon'$.
3. Tame valuations: $t \cdot \sum_{P \in Q} v(\psi(\tau_P) - 1) \leq \varepsilon'$, where $\tau_P$ generates tame inertia at $P$ and $t$ is a constant of $D$.
4. Lattice indices: for a family $F$ of lattices, the index of each twisted lattice in the base change exceeds the untwisted index by at most $\varepsilon_B(j, b)$, with $\sum_{j, b} \varepsilon_B(j, b) \leq \varepsilon'$.

**Definition 2.10.2 (admissible index bound for all powers).** The admissible index bound for all powers holds if for every index $i$ with a nonzero index place, if the set hypotheses hold at $i$, then for every $\varepsilon' > 0$, every family $F$ that satisfies the lattice hypotheses and every finite set $A_0$ of places, there are $Q$, $k$ and $\psi' : \mathrm{RCG}(Q) \to O_k^\times$ such that for every integer $a$ prime to $\ell$, the twist $\psi'^a$ is admissible for $A_0$ and has bounds within $\varepsilon'$.

A good twist adds to these conditions the inclusion of the twisted Eisenstein lattices into the base change of $V_0$, for a fixed basis $S$ of the sets $\Sigma_{i,j,b}$. The statement that good twists exist for all coprime powers is the same as the admissible index bound, with good twists in the conclusion.

### The choice of the character

**Theorem 2.10.3 (admissible index bound for all coprime powers).** Assume four statements: the existence of ray class characters with given coordinates at the auxiliary places, the lattice index statement for twists, the Selmer statement at auxiliary places, and the admissibility package of local conditions. Then the admissible index bound for all powers holds.

Lean: `GlobalTheory.TwistChoiceAll.admissibleIndexBoundAllPowers_of_conditions`.

*Proof.* Fix $i$, $\varepsilon'$, $F$ and $A_0$. Choose a tame inertia element $z$ at the twist prime.

Step 1: polynomials. The Selmer statement at auxiliary places, applied to the set of good signs, gives integers $R$, $D_0$ and $M_0$. For every level $M \geq M_0$ and every open normal subgroup $H'$ it gives $2R$ auxiliary places $P_q$ that avoid a given finite set, and for each good sign $s$ a polynomial $F_s$ in $2R$ variables with the following property. For any $k$ and any $u_q \in O_k^\times$ with $u_q^{\ell^M} = 1$, the Selmer length of the twist by $\psi = \prod_q u_q^{d_q}$ is $v(F_s(u_q - 1))$, and $F_s$ has a coefficient of degree at most $D_0$ with valuation at most $v(\ell^\nu)$. The theta statement gives, for each $\lambda$, an open normal subgroup $H_\lambda$ and a polynomial $f_\lambda$ with $f_\lambda(u_q - 1) = \ell^{N_0(i)} \theta_\lambda(\psi)$ and a controlled low coefficient. The lattice index statement gives the same for the lattice indices, with subgroups $H_{j,b}$ and polynomials $f_{j,b}$. Take $H'$ to be the intersection of the $H_\lambda$ and the $H_{j,b}$; it is open and normal. The statement on ray class characters gives the coordinates $d_q$, and $Q$ is the set of the places $P_q$ and their conjugates, so $|Q| \leq 4R$.

Step 2: the constant. Put $C = |\Sigma_G| + 2m + 4tR + 1$ and $\varepsilon = \varepsilon'/C$.

Step 3: the level. Substitute $x_q = (1 + X)^{\ell^{e_q}} - 1$ in each polynomial. If the exponents $e_q$ are spaced far apart, the polynomial in one variable $X$ keeps a coefficient of bounded degree $W$ with the same valuation bound. For a polynomial $h$ with such a coefficient and a primitive $\ell^k$-th root of unity $\zeta$, one has $v(\zeta - 1) = 1/\varphi(\ell^k)$. For all $k$ outside a finite set, the Newton polygon of $h$ shows that $h(\zeta - 1) \neq 0$ and
$$v(h(\zeta - 1)) \leq \frac{\mu}{v_O(\ell)} + \frac{W}{\varphi(\ell^k)}.$$
So there are $M \geq M_0$, $k \leq M$ and exponents $e_q < k$ with $\ell^{e_q}/\varphi(\ell^k) \leq \varepsilon$ such that for every primitive $\ell^k$-th root of unity $\zeta$, all evaluations at $u_q = \zeta^{\ell^{e_q}}$ are nonzero and exceed their low coefficient bound by at most $\varepsilon$.

Step 4: the character. Let $\chi_0$ be the character of $\prod_{P \in Q} (\mathbb{Z}/\ell^M)$ that sends the $q$-th coordinate to $\zeta_k^{\ell^{e_q}}$. Since $k \leq M$, it is well defined. By class field theory it factors as $\chi_0 = \psi' \circ \varphi$ through the ray class group, and we take this $\psi'$.

Step 5: all powers. Let $a$ be prime to $\ell$. Then $\zeta = \zeta_k^a$ is again a primitive $\ell^k$-th root of unity, and $\psi'^a$ is the character built in Step 4 from $\zeta$ in place of $\zeta_k$. So it suffices to check the conditions for the character built from an arbitrary primitive root $\zeta$ in $\langle \zeta_k \rangle$.

The Selmer length for the sign $s$ is $v(F_s(\zeta^{\ell^{e_q}} - 1)) \leq \nu + \varepsilon$, so condition 1 holds with $\varepsilon_T(s) = \varepsilon$ and $\sum_s \varepsilon_T(s) \leq |\Sigma_G| \varepsilon$. The theta value is nonzero, and $v(\theta_\lambda) = v(f_\lambda) - N_0(i)$ lies between $-N_0(i)$ and $c_0(\lambda) + \varepsilon$. The lattice indices give condition 4 with total at most $2m\varepsilon$. For the tame part, $\zeta^{\ell^{e_q}}$ is a primitive $\ell^{k - e_q}$-th root of unity, so
$$v(\zeta^{\ell^{e_q}} - 1) = \frac{1}{\varphi(\ell^{k - e_q})} = \frac{\ell^{e_q}}{\varphi(\ell^k)} \leq \varepsilon,$$
and $t \sum_{P \in Q} v(\psi(\tau_P) - 1) \leq 4tR\varepsilon$. Each of these totals is at most $C\varepsilon = \varepsilon'$.

Admissibility: the places of $Q$ come from the Selmer statement, so they are split of degree one and avoid $A_0$. The character takes values in $\langle \zeta_k \rangle$. Each $u_q = \zeta^{\ell^{e_q}}$ is different from $1$ because $e_q < k$, so $\psi$ is ramified at every place of $Q$ and at no other place. The coordinates $d_q$ are trivial above $\ell$ and satisfy the conjugation rule, so $\psi$ does too. $\square$

The proof never uses that $\zeta$ is the fixed root $\zeta_k$. That is why one choice of $Q$, $k$ and the exponents serves every power at once.

### Good twists from the Selmer and lattice inputs

**Theorem 2.10.4 (good twists from the Selmer and sup-lattice inputs).** Let $E$ be a Hecke datum over $D$ and $N_0$ a function on the twist indices. Assume the Selmer presentation, the residual order bound for $\nu = 0$, the order bound for $\nu > 0$, the admissibility package and the statement on ray class characters. Assume also the relation between theta values and Hecke eigenvalues, the commutation of Hecke operators, the vanishing of eigenvalues off range, the goodness of all twist data, the eighth admissibility condition, six conditions on the sup lattices and the Hecke action on them, a condition on the fourth admissibility clause, the specialization of twisted series, the signature condition and the semisimplicity of the Hecke action. Then for every twist index $i$ with a nonzero index place, good twists exist for all powers prime to $\ell_i$.

Lean: `GlobalTheory.TwExportSup.twistTheorem_allPowers_of_selmer_supLattice`.

*Proof.* The Selmer presentation gives a matrix $\Phi$ that computes the Selmer data. The Selmer lengths equal the valuation of $\det \Phi$ after specialization, so every polynomial that represents $\det \Phi$ is a Selmer polynomial. The two order bounds give a low coefficient of valuation at most $v(\ell^\nu)$, for $\nu = 0$ and for $\nu > 0$. Together this is the Selmer statement at auxiliary places. The relation between theta values and eigenvalues, with the Hecke laws that follow from commutation and the off range condition, gives the lattice index statement. The previous theorem gives the admissible index bound for all powers. The lattice conditions give the decomposition of the module of forms into the internal direct sum of its isotypic parts, and the commutation condition on the group gives the integrality of the group algebra. With the semisimplicity of the Hecke action these give good lattice points. The admissible index bound, the direct sum, the integrality, the fourth admissibility clause, the specialization and the good lattice points turn an admissible twist with bounds into a good twist. $\square$

### The statement from Galois cohomology and class field theory

**Theorem 2.10.5 (good twists from Galois cohomology and class field theory).** Assume the Chebotarev density theorem, Poitou-Tate duality for totally complex fields, cohomological dimension two, the tame local statements, local finiteness, local Tate duality, the local and global Euler characteristic formulas, global finiteness, the orthogonality of unramified classes, the six-part duality statement, the Greenberg-Wiles formula and the existence of ray class characters through the Artin map. Assume also the 22 conditions on $D$ and $E$ of the previous theorem and of the admissibility package. Then for every twist index $i$ with a nonzero index place, good twists exist for all powers prime to $\ell_i$.

Lean: `GlobalTheory.TwExportTop.twistAllPowers_of_galoisCohomology_classField`.

*Proof.* Apply the previous theorem. Its inputs come from the hypotheses as follows.

1. The Selmer presentation is the theorem on Selmer presentations of the previous section.
2. The residual order bound for $\nu = 0$ follows from the auxiliary place argument for odd residual data and the Greenberg-Wiles formula.
3. The order bound for $\nu > 0$ is the order bound of the previous section.
4. The admissibility package is assembled from four admissibility conditions on $D$, the six-part duality statement and the dimension formula that local duality gives from the fifth local conclusion.
5. The statement on ray class characters follows from the universality of the characters. Its proof constructs admissible families of ray class characters and uses the Artin map for them.

The other conditions pass unchanged. $\square$

**Remark 2.10.6 (Formalization).** The first theorem is in [AdmissibleIndexBoundAllPowersOfConditions.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/AdmissibleIndexBoundAllPowersOfConditions.lean#L92). Step 3 is `exists_level` in [IsAuxiliaryPlaceFamilyAtLevelMono.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsAuxiliaryPlaceFamilyAtLevelMono.lean#L321), which reduces to `GlobalTheory.OrderEval.order_eval` in [ExistsLevelOrderExponentsSmallValuationDetermina.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsLevelOrderExponentsSmallValuationDetermina.lean#L278). Step 5 uses `zpow_prim` and `psiOk_partD_root` (lines 31 and 38). The same file has `admAB_of_toric_parts` ([line 355](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IsAuxiliaryPlaceFamilyAtLevelMono.lean#L355)), which repeats most of the proof for the single character $\zeta_k$. At line 98 the proof discards the component `ArchimedeanSignatureMatching` of `AdmACD`, and it discards the last conjunct $2r \leq g(k)$ of `SetHyp`. The conclusions `admissibleIndexBoundAllPowers` and `goodTwistExistsAllCoprimePowers` are in [AdmissibleIndexBoundAllPowers.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/AdmissibleIndexBoundAllPowers.lean#L14) (line 14 and [line 23](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/AdmissibleIndexBoundAllPowers.lean#L23)), in the namespace `GlobalTheory.TwAll`. The second theorem is in [TwistTheoremAllPowersOfSelmerSupLattice.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TwistTheoremAllPowersOfSelmerSupLattice.lean#L24) and ends with `GlobalTheory.exportAll_of_six_inputs`. The third theorem is in [TwistAllPowersOfGaloisCohomologyClassField.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TwistAllPowersOfGaloisCohomologyClassField.lean#L20). The conditions of the twist are `PsiOk`, `partAT`, `partC` and `partD` in [BlochKatoPhases.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/BlochKatoPhases.lean#L289), and `partAB` is in `IntegralHeckeForms`. The set hypotheses `SetHyp` ([BlochKatoPhases.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/BlochKatoPhases.lean#L327)) begin with a conjunct `True` and ask $r \geq 100$; the proof passes that `True` on to `GalHyp`. The hypothesis `Gen.ArchimedeanSignatureMatching` ([BlochKatoPhases.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/BlochKatoPhases.lean#L400)) is the conjunction of a Poitou-Tate cokernel statement, a Sha statement, an $H^2$ duality statement and three local statements; nothing in it is archimedean. The Lean names of the Selmer theorems in the proof are `selmerPresentationMatrix_of_galois_cohomology`, `residualSelmerBound_of_auxiliaryPrimes_odd`, `boundModTwoUniformizerAtTwo_of_chebotarev`, `duality_dim_of_localTheorem` and `delUTie_of_isUnivChar`.

## Notes and references

This chapter feeds two steps of the proof directly and three results of other volumes. The first inequality and the global reciprocity law of Sections 1 and 2 enter [EveryCharacter from the Galois row](/step/every-character/). The main theorem of complex multiplication of Section 3 and the base case of Poitou-Tate duality for restricted ramification of Sections 4 and 5 enter [EveryCharacter from Row0b](/step/every-character-of-row/). The vanishing in high degrees and the duality with real places of Sections 6 and 7 give the bijectivity of restriction to the real places, which enters [the Euler ratio is one, from its coprime case](/entry/ratio-one-of-lemma-x/). Section 8 gives [the bound for unramified linear data](/entry/lin-dat-unram-bound/). Sections 9 and 10 give the good twists for [the local export condition from rational rows](/entry/export-at-of-bundles-alt/).

1. J. Neukirch, A. Schmidt and K. Wingberg, *Cohomology of Number Fields*, 2nd ed., Grundlehren 323, Springer, 2008, Ch. VIII §§3, 6.
2. J. S. Milne, *Arithmetic Duality Theorems*, 2nd ed., BookSurge, 2006, Ch. I §4 (Theorem I.4.10) and Ch. II §2.
3. J. Tate, Duality theorems in Galois cohomology over number fields, Proc. ICM Stockholm 1962, Inst. Mittag-Leffler, 1963, 288 to 295.
4. J.-P. Serre, *Galois Cohomology*, Springer, 1997, Ch. II §6.
5. J. Neukirch, *Algebraic Number Theory*, Grundlehren 322, Springer, 1999, Ch. VI §§1 to 6 and Ch. VII §13.
6. J. H. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, GTM 151, Springer, 1994, Ch. II Theorem 8.2.
7. G. Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions*, Princeton University Press, 1971, Theorem 5.4.

Sections 1 and 2 follow [5], Ch. VI. Section 3 follows [6] and [7]. Sections 4 to 7 follow [1], [2], [3] and [4]. No classical source is known to us for the theorem on the unramified cokernel length in Section 8. The constructions of Sections 9 and 10 use the Euler characteristic formulas and Poitou-Tate duality of [1] and [2], and the Chebotarev density theorem of [5], Ch. VII §13.
