---
title: Congruence bounds and joint conditions
decls:
  - GlobalTheory.T.eventually_congBound_of_facts
  - GlobalTheory.NLinkE.main_alt_alt
  - GlobalTheory.T.embedding_jumps_aux2_of_setup
  - GlobalTheory.TheoremBQD.main_alt_alt
  - GlobalTheory.HTW.RecS.fam_jointBCD_closed_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Congruence bounds and joint conditions

This section proves three inputs of [the closing conclusion](/entry/nlink-close-main-alt-alt/) of Section 8. The first is the congruence bound at the large primes, eventually along a family. The second is the bound at the two ramified primes $q$ and $d$, with an explicit constant and polynomial. The third is a threshold past which the joint hub conditions hold. Each result passes the published local inputs to a lemma with the content: [the Selmer length bound at twisted places](/entry/twisted-place-selmer-length-bound-of-local-duality/) for the second, and [the joint hub conditions of a family](/entry/fam-joint-bcd/) for the third.

We keep the notation of Section 8. For a datum $D$ and a point $\pi$ at an index $k$, the *congruence valuation* $v_{\mathrm{CC}}(\pi) \in [0, \infty]$ is the infimum, over the congruence elements $f$, of the normalized length of $O/(f(\pi))$. The *Selmer length* $s_\pi$ is the normalized length of a [[Selmer group|36YNSTESMQ]] at $\pi$, and $\operatorname{len} Ш_e$ is the length of the Tate-Shafarevich group of the twist $e$. The class number of $E$ is $h_E$.

**Definition 8.9.1 (The congruence bound).** Let $D$ be a datum with size data $L$. The *congruence bound* for $D$ and $L$ says the following. Let $k$ be an index of $D$ with prime $\ell = \ell_k$ such that $\ell > \ell^*(L)$, $\ell \neq g_j$ for all $j$, $\ell$ is not in the exceptional set $\mathrm{Exc}(L)$, the weight tie holds and the host condition holds. Let $r$ be a good family, $\pi \in Z_k$ and $\rho$ a part of rank $r$ of $r(\pi)$. Then, in $[0, \infty]$,

$$v_{\mathrm{CC}}(\pi) \le s_\pi + \sum_{0 < e < t} \operatorname{len} Ш_e + v_\ell(h_E) + t \sum_{P \in Q_k} v(\zeta_P - 1).$$

Here $\mathrm{Exc}(L)$ is the set of primes above $\ell^*$ that divide an integer in a window around one of the base sizes, and $Q_k$ is the set of auxiliary primes at $k$.

**Theorem 8.9.2 (The congruence bound along a family).** Assume the published local inputs. Let $F$ be a family. Then there is $x_0$ such that for each $x \ge x_0$ with $x > x_1$ and each index $i$ at $x$, if the norm choice facts hold at $D_{x,i}$, then the congruence bound holds for $D_{x,i}$ and $L_{x,i}$.

Lean: `GlobalTheory.NLinkE.main_alt_alt` (also `GlobalTheory.T.eventually_congBound_of_facts`, a second name).

*Proof.* Let $x_0$ be the largest of three thresholds. Past the first, $\ell \ge 5$, $\ell > t + 1$, $\ell \neq q, d$, $\ell$ is not small, and there are position data off the exceptional primes. Past the second, the jump conditions hold. Past the third, the parameters are admissible.

Fix $k$, $r$, $\pi$ and $\rho$. The host field is unramified at $\ell$. The lemmas at large good places give the first three admissibility conditions, the second with Fontaine's ring $B_{\mathrm{cris}}$, and they give continuity and semisimplicity. The inertia at a cyclotomic generator gives a decomposition by orthogonal idempotents. The integrality input of Bhatt and Scholze gives a Wach functor and a comparison. [Local Bloch-Kato theory](/learn/padic-hodge/#local-bloch-kato-theory), local Tate duality and the local Euler characteristic give the top condition and local bounds above $\ell$. When the Selmer and Tate-Shafarevich groups are finite, the global count of congruences, with global [[Artin reciprocity|7938EKMMVR]], gives a rational bound. A rational bound under these finiteness conditions gives the bound in $[0, \infty]$ with no condition. $\square$

The weight tie and local finiteness are not used.

**Theorem 8.9.3 (The bound at $q$ and $d$).** Let $C = 2080$ and $Q = 260\, X_0^2 X_2^2 (X_1 + X_2)$. Assume the published local inputs. Let $D$ be a datum, $L$ size data and $X$ hub data in setup with some $C_2$. Let $i$ be a twisted index with $\ell = \ell_i \in \{q, d\}$ and $\ell > x^{2C_t + 5}$, where $x$ and $C_t$ come from $L$. Let $\pi$ be a good point, and assume that the Selmer group at $\pi$ and the groups $Ш_e$ for $0 < e < t$ are finite. Then

$$v_{\mathrm{cc}}(\pi) \le B_\ell + \sum_{0 < e < t} \operatorname{len} Ш_e + v_\ell(h_E) + s_\pi + \ell^{-2},$$

where

$$B_\ell = C f \bigl( r (b/\ell + S_c + t + \eta + \log b) + m b \bigr) + Q(f, r, t) \log b.$$

Here $f$, $r$, $t$ and $m$ are integers of $D$, and $b$, $S_c$ and $\eta$ are sizes of $L$.

Lean: `GlobalTheory.TheoremBQD.main_alt_alt` (also `GlobalTheory.T.embedding_jumps_aux2_of_setup`, a second name).

*Proof.* This is [the Selmer length bound at twisted places](/entry/twisted-place-selmer-length-bound-of-local-duality/), once its inputs are checked.

1. The admissibility conditions $G_1$ to $G_6$, the tame generator conditions and the Iwahori condition at $\ell \in \{q, d\}$ hold by the setup, since $\ell \notin \{g_0, g_1\}$.
2. The lattice index theorem follows from the row conditions, Artin reciprocity, local Bloch-Kato theory, local Tate duality and the local Euler characteristic.
3. The condition at twisted places is the killing condition of the setup.
4. The Hodge jumps come from the setup.
5. The inequality $260 f^2 t^2 (r + t) \le Q(f, r, t)$ holds since $Q(f, r, t) = 260 f^2 t^2 (r + t)$.

Conditions that do not depend on $\pi$ use a chosen good point. The Selmer length bound has three conclusions, and we keep the third. $\square$

The condition $\ell > x^{2C_t + 5}$ asks a prime of the host to be large compared to the scale. We did not check when it can hold.

**Definition 8.9.4 (Inputs at the places over $\ell$).** *Fontaine's ring* is a list of properties of $B_{\mathrm{cris}}$ at each prime $\ell$ and each core, for example that $\varphi - 1$ maps the elements of $\mathrm{Fil}^0$ onto $B_{\mathrm{cris}}$. A datum is *closed for jumps* if each parameter $L$ with the jump admissibility satisfies the jump conditions. A family has *point families* at $X$ if $X.r$ and $X.\rho$ are families of points of $D$.

**Theorem 8.9.5 (Joint hub conditions along a family).** Assume Fontaine's ring. Assume that each datum satisfies the seventh admissibility condition and the Fontaine condition at the places over $\ell$, and that each datum is closed for jumps. Let $F$ be a family and $R$ a row. Then there is $x_0$ such that for $x \ge x_0$ with $x > x_1$, each index $j$, each local datum and each hub datum $X$ of $D_{x,j}$: if $L_{x,j}$ has the jump admissibility and $X$ has point families, then the joint hub conditions hold for $L_{x,j}$, $X$ and $R$.

Lean: `GlobalTheory.HTW.RecS.fam_jointBCD_closed_alt`.

*Proof.* [The joint hub conditions of a family](/entry/fam-joint-bcd/) give $x_0$ from the seventh admissibility condition and the Fontaine condition. At each member they need two more facts.

1. The first jump conclusion. This is the first part of the jump conditions, so it follows from closure for jumps and the jump admissibility.
2. The point input at each good $\pi$ and each inert index $i$. The point families, the first part of the jump admissibility (the family is de Rham away from the type primes) and Fontaine's ring give it, once $\ell_i \notin \{g_0, g_1\}$. An inert prime is not a type prime, so this holds. $\square$

**Remark 8.9.6 (Formalization).** The congruence bound is `CongBound_at`, and the theorem is at [AdmissibleParameterEventually.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AdmissibleParameterEventually.lean#L30); there the weight tie is the hypothesis `_hW`, which is never used, and `LocalFinitenessK` is not used. The third threshold is the private lemma `admissible_parameter_eventually`. The bound at $q$ and $d$ is `EmbeddingTypeJumps.Conclusion2`, proved at [MainOfAltAlt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainOfAltAlt.lean#L55) by `main_of_alt` applied to `twistedPlace_selmerLengthBound_of_localDuality`; the hypothesis `hc` of [main_of_alt](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainOfAltAlt.lean#L18) is the statement of that proved lemma, so the split adds nothing. $Q$ is `polyB`, and its inequality is `polyB_val`. The second name `embedding_jumps_aux2_of_setup` has "aux2" from `Conclusion2`; the statement has no embedding and no jumps, and its file name `PolynomialBoundSetup` is also the name of another file, under `Proofs/InertiaEigenvalues`, which defines `polyB`. `TwLoc` is defined twice, in `EmbeddingTypeJumps` and in [TwistedPlaces.lean](lean:Development/AutomorphicArithmetic/ResidueCharacters/TwistedPlaces.lean#L77), with the same meaning. The joint conditions are at [FamJointBCDClosed.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamJointBCDClosed.lean#L13): `ConclusionJa` comes from `JumpClosed`, and `PtIn` from `ptIn_of_ptFam_deRham_away` with `inert_prime_ne_typePrime`; the fact `TwLoc` that `fam_jointBCD` provides is not used.
