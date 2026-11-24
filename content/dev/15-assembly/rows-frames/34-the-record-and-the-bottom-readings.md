---
title: The record and the bottom readings
decls:
  - GlobalTheory.MemLoc.record_nonempty
  - GlobalTheory.StdRead.reads_std
  - GlobalTheory.BotSmallDict.reads_datum
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The record and the bottom readings

This section has two parts. The first closes the construction of Sections 24 and 25: it builds the local period data at every prime, and so shows that there is a datum at all. The second proves two reading statements for the bottom of the triangles of theta functions. Each says that a theta function built from a coset indicator restricts, at the archimedean points, to a Gaussian times a known holomorphic function, up to a constant of absolute value one.

### Local period data

For a prime $\ell$ let $\mathbb{C}_\ell$ be the completion of an algebraic closure of $\mathbb{Q}_\ell$, $\mathcal{O}$ the integral closure of $\mathbb{Z}_\ell$ in it, and $A_{\inf}$, $A_{\mathrm{cris}}$, $B_{\mathrm{cris}}$, $B^+_{\mathrm{dR}}$ and $B_{\mathrm{dR}}$ the period rings of Fontaine, with their actions of $G_{\mathbb{Q}_\ell}$ and the Frobenius on the crystalline rings. A *core* at $\ell$ consists of:

1. a compatible system $(\zeta_m)_{m \geq 0}$ of $\ell^m$th roots of unity with $\zeta_0 = 1$ and $\zeta_1 \neq 1$, and an element $\varepsilon$ of the tilt whose untilts of the roots are the $\zeta_m$;
2. a section $\mathcal{O} \to B^+_{\mathrm{dR}}$ of the map $\theta$;
3. the canonical map $j \colon A_{\mathrm{cris}} \to B^+_{\mathrm{dR}}$, and an injective map $\iota \colon B_{\mathrm{cris}} \to B_{\mathrm{dR}}$ compatible with $j$;
4. a map from the maximal unramified extension to $B_{\mathrm{cris}}$ compatible with the section;
5. an element $t \in A_{\mathrm{cris}}$ that is a logarithm of $[\varepsilon]$;
6. the arithmetic Frobenius $\sigma$ of the maximal unramified extension, and the cyclotomic character $\chi \colon G_{\mathbb{Q}_\ell} \to \mathbb{Z}_\ell^\times$.

From a core one builds a *local prime*: a pair of rings $B$ and $B_{\mathrm{dR}}$ with a Galois action, a Frobenius, an inclusion $B \to B_{\mathrm{dR}}$, a filtration and a period $t$; an $A_{\inf}$ structure on it; and a *tie*, an isomorphism of $B$ with $B_{\mathrm{cris}}$ and of $B_{\mathrm{dR}}$ with the standard $B_{\mathrm{dR}}$ that respects the integers, the Galois actions, the Frobenius and the inclusion. A choice of a local prime with $A_{\inf}$ structure and tie at every $\ell$ is the *local gap* $\mathrm{LG}(H)$ of Section 24. Its fields do not depend on the host $H$.

**Theorem 7.34.1 (There is a datum).** The type of data is nonempty.

Lean: `GlobalTheory.MemLoc.record_nonempty`.

*Proof.* At each prime $\ell$ a core exists. The compatible roots and the element $\varepsilon$ exist by the construction of the tilt, the section of $\theta$ and the map $j$ by the universal property of $A_{\mathrm{cris}}$, and $\iota$ by the localization that defines $B_{\mathrm{cris}}$ and $B_{\mathrm{dR}}$. From the core we build a local prime, its $A_{\inf}$ structure and its tie. Choosing one at each prime gives an element of $\mathrm{LG}(H)$ for every host $H$, and in particular for the host $H_0$. By [the theorem of Section 24](/entry/record-nonempty-of-local-gap/), an element of $\mathrm{LG}(H_0)$ gives a datum, namely the example record of Section 25. $\square$

The proof of existence of the core cites lemmas for each of its fields: the roots and the tilt, the section of $\theta$, the map $A_{\mathrm{cris}} \to B^+_{\mathrm{dR}}$ and the injectivity of $B_{\mathrm{cris}} \to B_{\mathrm{dR}}$. The reasons given above are the classical constructions of Fontaine, not the Lean proofs. The theorem is used by [the choice of global positions](/entry/exists-positions-global/), which needs one datum to start from.

### Readings

Fix a datum $D$ with the host fields $K \subseteq E$, and an infinite family $\theta$ of the real data. For hermitian spaces $S$ and $T$ of ranks $a$ and $d$, let $W_O(S, T)$ be the adelic matrix space of the Weil representation, and $\mathrm{VC}(a, d)$ the space of families $(Z_\tau)$ of complex $d \times a$ matrices, one for each archimedean index $\tau$. For $\delta \in \mathbb{C}$ and $r \in E$, the *coordinates* of a point $w$ are
$$Y(w)_\tau = \delta\, \tau(r)\, w_\tau,$$
where $w_\tau$ is the component of $w$ at $\tau$ read through $\theta$. Let $H_\delta$ be the hermitian form of the torus of $\delta$ on $\mathrm{VC}(a, d)$.

**Definition 7.34.2 (Reading).** A function $f$ on $W_O(S, T)$ *reads* a function $G$ on $\mathrm{VC}(a, d)$ if $f$ is a theta function and
$$f(w) = \exp\Bigl(-\frac{\pi}{2}\, H_\delta\bigl(Y(w), Y(w)\bigr)\Bigr)\, G\bigl(Y(w)\bigr)$$
for every $w$ with trivial finite part.

Readings are additive and homogeneous: if $f_k$ reads $G_k$ for each $k$ in a finite set, then $\sum_k f_k$ reads $\sum_k G_k$, and $c f$ reads $c G$. A complex number $u$ is a *phase* if $|u| = 1$, $u$ is algebraic, and $|\lambda(u)|_p = 1$ for every prime $p$ and every embedding $\lambda \colon \overline{\mathbb{Q}} \to \mathbb{C}_p$. A root of unity is a phase, and so is its complex conjugate.

### The standard first function

A *pair* $P$ of the datum, for the torus of $\delta$ and a level $Q$, has ranks $a$ and $d$, an odd vector $e_0$, a test vector $F$, and a Weil datum. For a good modulus $\mathfrak{m}$ at an idempotent $e$, a unitary Hecke character $\nu$ that is trivial on the congruences mod $\mathfrak{m}$, and a frame $\beta$ of the standard lattice, the *standard first function* is a function on $W_O(S, T)$ built from $\nu$, $e$, $\mathfrak{m}$ and $\beta$; it is a sum of characters times indicators of cosets mod $\mathfrak{m}$. A place model operator $T_m$ at $e$ moves functions of the local coordinates to theta functions.

**Theorem 7.34.3 (Reading the standard first function).** Let $P$ be a pair with $S$ and $T$ of ranks $a$ and $d$, the class group condition $\mathfrak{c}_K = \top$, and the standard setup. Let $v$ be the vacuum vector for the standard lattices, and $c$ a constant such that $c\, e_0$ is a theta vector of the torus and $v$ reads $c\, e_0$. Let $\mathfrak{m}$, $\nu$ and $\beta$ be as above, with $\nu^{-1}$ having the finite part of the Weil datum of $P$, and assume that $P$ is a standard datum for $\mathfrak{m}$. If $f$ is the image under $T_m$ of the complex conjugate of the standard first function, then there is a phase $u$ such that $f$ reads $(c u)\, F$.

Lean: `GlobalTheory.StdRead.reads_std`.

*Proof.* We follow the Lean proof.

1. Since $P$ is a standard datum, there is a finite set $R$ of integral group elements with
$$F = \sum_{r \in R} \omega(r)\, \mathrm{cos}(r),$$
where $\mathrm{cos}(r)$ is the coset vector of $r$ and $\omega$ the Weil action of the pair.
2. The frame $\beta$ is an integral matrix for the completed standard lattice, and the value of $\nu$ on its determinant has finite order: there is $m > 0$ with $\nu(\det \beta)^m = 1$. Let $u$ be the complex conjugate of this value. It is a phase.
3. For each $r \in R$ choose an integral element $z_r$ that approximates $r$ mod $\mathfrak{m}$.
4. The indicator of the ideal $\mathfrak{m}$ reads a norm power times the intertwined vacuum, and from this, the indicator of the coset of $z$ reads the translate by $z$ of the curve theta function.
5. The complex conjugate of the standard first function is the sum over $r \in R$ of the coset indicators of $z_r$, times $u$.
6. The integral point $r$ acts on the coset vector through the unit character, and $\omega(r)\, \mathrm{cos}(r)$ is the coset vector of $z_r$ times the eigenvalue.
7. Summing over $R$ with the additivity of readings, and scaling by $c u$, gives that $f$ reads $(c u)\, F$.

This proves the theorem. $\square$

The theorem is the reading step of [the bottom datum of the standard module](/entry/standard-module-bottom-datum/).

### The second bottom function

A *bottom triangle* $X$ for a Weil datum $W$ and indices $i, j$ consists of hermitian spaces $A$, $A'$ and $W'$, self-dual standard lattices, frames and vacuum vectors $v'$, and for each index $s$ a second function $f'_s$ on $W_O(A', W')$. A pair $(P, P')$ is a *bottom pair* at $s$ if it fits the triangle at the modulus of $s$.

**Theorem 7.34.4 (Reading the second bottom function).** Let $X$ be a bottom triangle with $\beta = 1$ on $W'$, and $(P, P')$ a bottom pair at $s$, with the ranks of $A'$ and $W'$ equal to those of $P'$. Assume that the vacuum $v'$ reads $\kappa\, e_0'$. Then there is a root of unity $\zeta$ such that $f'_s$ reads $(\kappa \zeta)\, F'$.

Lean: `GlobalTheory.BotSmallDict.reads_datum`.

*Proof.* We follow the Lean proof.

1. The record of the datum gives $\mathfrak{c}_K = \top$, and the triangle gives the standard setup and the Weil datum of the second side. The idempotent of $s$ is good: its places are prime to $2 q d$.
2. The conductor exponents of the square character at $s$ are positive, and their product is the modulus $\mathfrak{m}_s$. So $\mathfrak{m}_s \neq 0$, and its conjugate is nonzero.
3. The half coset indicators mod the conjugate of $\mathfrak{m}_s$ are Schwartz-Bruhat functions on the half.
4. The level indicator reads a norm power times a unit vector, with a root of unity $\zeta_1$, and the conjugate ideal indicator translated by the unit block reads through the Weil operator, with a root of unity $\zeta_2$. So the image of the coset function reads $\zeta_2 \kappa \zeta_1$ times the coset vector of $P'$.
5. Since $(P, P')$ is a bottom pair, there is a finite set $R$ with $F' = \sum_{r \in R} \omega(r)\, \mathrm{cos}$, and the second function is, up to a root of unity $\zeta_3$, the sum over $R$ of translates of the coset function by finite points $g_r$ with Gram matrix one.
6. Each translate reads $\zeta_2 \kappa \zeta_1\, \omega(r)\, \mathrm{cos}$, by the action of the Weil datum on the place model and on the vacuum.
7. Summing over $R$ and scaling by $\zeta_3$ gives that $f'_s$ reads $(\kappa \zeta)\, F'$ with $\zeta = \zeta_3 \zeta_2 \zeta_1$.

This proves the theorem. $\square$

The theorem is the reading step of [the bottom kernel as a class sum](/entry/bottom-kernel-eq-class-sum-term/). There the kernel is computed from the reading, and the constant $\kappa \zeta$ becomes the constant of the term.

**Remark 7.34.5 (Formalization).** The theorem `record_nonempty` is at line 14 of [LocalGapNonemptyAndRecordNonempty.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalGapNonemptyAndRecordNonempty.lean#L14); it is `record_nonempty_of_localGap (localGap_nonempty _)`, and `localGap_nonempty` at line 8 takes a host and does not use it. It calls `exists_locTheory_tied` at line 8 of [ExistsLocTheoryTied.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ExistsLocTheoryTied.lean#L8), which chooses from `exists_locPrime_tied` at line 281 of [ExistsLocalPrimeAinf.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsLocalPrimeAinf.lean#L281). That one uses `nonempty_core` at line 48 of [NonemptyLocalPeriodRingsData.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/NonemptyLocalPeriodRingsData.lean#L48) and the constructions `PrimeEx.prime`, `PrimeEx.ainf` and `PrimeEx.tied` of the same file as `exists_locPrime_tied`. The structure `Core` is at line 52 of [IsCrisP.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/IsCrisP.lean#L52), and `LocTied` at line 11 of [LocTied.lean](lean:Formalism/LocalRingCardinality/AdicCompletionLocal/LocTied.lean#L11). The theorem `reads_std` is at line 129 of [BottomTriangleUnitConstant.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/BottomTriangleUnitConstant.lean#L129), with `IsPh` at line 83 and `isPh_of_pow` at line 104. Its proof is used twice in the same form, at line 271 of the same file and at line 115 of [StandardModuleBottomDatumExists.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/StandardModuleBottomDatumExists.lean#L115). `Reads` is at line 29 of [IsCongLevelIntG.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsCongLevelIntG.lean#L29). The theorem `reads_datum` is at line 309 of [BottomTriangleNonzeroConstantSecond.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/BottomTriangleNonzeroConstantSecond.lean#L309), under `maxHeartbeats 1600000`. It reads $\mathfrak{c}_K = \top$ off the record by the projection `hR.size.2.2.2.2.2.2.2.2.2.2.2.2.2` (line 313), which depends on the order of thirteen fields. Its user `kernel_eq_term` at line 404 of the same file has a copy at line 59 of [SmallStageBottomKernelEqTerm.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/SmallStageBottomKernelEqTerm.lean#L59). Steps 4 to 6 of both reading proofs are cited lemmas, such as `cosetIndicator_reads_as_translate_curveTheta` and `level_indicator_reads_norm_power_unit_vector`; we describe what they state and did not open them.
