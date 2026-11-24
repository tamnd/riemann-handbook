---
title: Comparison choices at all places
decls:
  - GlobalTheory.LevCmp.stageCExists_of_harishChandra_serN
  - GlobalTheory.T.stageCExists_of_casselmanWallach
  - GlobalTheory.ChoiceRead.exists_stC_choice_alt
  - GlobalTheory.T.nonGalois_exists_choice_alt
  - GlobalTheory.PlaceRead.exists_local_map_at_place_alt
  - GlobalTheory.T.local_component_at_place_determined_alt
  - GlobalTheory.PlaceRead.exists_basisAt_latAt_thetaAt_of_atPlace
  - GlobalTheory.PlaceRead.exists_local_component_at_place_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Comparison choices at all places

This section proves item 5 of [the stage statements](/entry/all-stages-of-specializations-alt/) of Section 6: each third level datum at a stage extends to a strict henselian acyclic level datum, for every admissible choice of twist indices at the places. The second nonvanishing statement of Section 13 uses it as one of its nine step statements. The work is local. At each twisted place we must compare the theta lift of a twisted level form with a class sum, and this comparison fixes the local component of the lift up to a unit. The comparison rests on the local theta correspondence in the Fock model and on the local tuple attached to a discrete series, which is where Harish-Chandra's theory enters.

We keep the notation of Sections 6, 9 and 11. Let $x$ be a stage of a datum $P$ of a column datum $w$ over a base $B$ with twist datum $T$, and let $D = D_x$. The datum $D$ has a CM field $E$, a coefficient field $L_0$, places $v$ with a conjugation $v \mapsto \bar v$, twist indices, and at each place $v$ a twist $\mu_v$. A place $v$ is *twisted* if $\mu_v \neq \mu_0$, the untwisted value.

We take the following as given. They are fields of $\mathcal{H}_A$ and $\mathcal{H}_M$ in Section 1.

1. Harish-Chandra's classification of the [discrete series](/learn/real-groups/#discrete-series-and-formal-degrees) (the discrete series cover): for $p + q \geq 1$ and each unitary group $U(p, q)$ there is a discrete series $D(\lambda)$ for each Harish-Chandra parameter $\lambda$, with the $K$-types attached to $\lambda$, and every discrete series is unitarily equivalent to some $D(\lambda)$.
2. The Casselman-Wallach theorem on the smooth Fréchet globalization of the Harish-Chandra module of an irreducible unitary representation of $U(p, q)$ ([representations of real groups](/learn/representations/#representations-of-real-groups)).
3. Harish-Chandra's theory of $(\mathfrak{g}, K)$-modules: for an irreducible unitary representation of $U(p, q)$, the $K$-finite vectors are smooth, a Harish-Chandra module exists, and every Harish-Chandra module of the representation is admissible and irreducible.

**Definition 6.12.1 (Choices and character data).** A *choice* $\mathrm{ch}$ for $D$ gives at each place $v$ a twist index $\mathrm{ch}_{\mathrm{tw}}(v)$, a weight $k'(v)$, a place $Q(v)$ above $v$, a character $\psi'(v)$, a local ring $\mathcal{O}_e(v)$ and an embedding $\mathrm{emb}_W(v)$. A *tied tuple* for $\mathrm{ch}$ is a tuple $t_p$ of local data with a character $\xi$ and a character $\psi$. The choice is *admissible* at a third level datum $l$ if $\xi$ is the character of $w$, $\psi$ is the character of $T$, $Q$ is the place map of $P$, $k'(v)$ is the weight of $T$ at each twisted place, the side condition holds for the moduli data of $l$, and the twist condition holds at each twisted place: the index $\mathrm{ch}_{\mathrm{tw}}(v)$ is good for the weight $k'(v)$, the place $Q(v)$ and the character $\psi'(v)$ composed with the Artin map of the twist. A *height counting character datum* $c$ over $l$ is a character datum for the moduli data and the base data of $l$, with the weight and character of $T$; it has a twist index map $c_{\mathrm{tw}}$.

**Definition 6.12.2 (Local maps at a place).** Let $v$ be a twisted place and $i$ an index with $1 \leq i \leq m$. Let $M_i(v)$ be the lattice of the twisted moduli forms at $v$ and weight $i$, and $T_i(v)$ the target space of the choice at $v$. A *local map* at $(v, i)$ is a map $e : M_i(v) \to T_i(v)$, semilinear over $\mathrm{emb}_W(v)$, with a unit $u$ of the fraction field of $\mathcal{O}_e(v)$, such that three conditions hold: $e$ sends a basis to a basis (the basis condition), $e(M_i(v))$ is $u$ times the standard lattice (the lattice condition), and $e$ sends the theta lift of a twisted level form to $u$ times the class sum of the series datum (the theta condition).

**Theorem 6.12.3 (Local component at a place).** Assume statements 1 to 3 and $\mathcal{P}$. Let $D$ be a datum with a real side $X$, a base level row side, a reading $Y$, rational data $S$, a real series datum $Y_S$, an export tie $Z$ with representation $\rho$, a choice $c$, a place $w$ and an index $j$, with the place data at $(w, j)$. Let $\varepsilon$ be a ring map from the field of $c$ at $w$ to $\mathbb{C}$ that extends $\rho$. Then there are a map $\Psi$ from the moduli lattice at $(\mu_w, j + 1)$ to the ambient space, semilinear over $\varepsilon \circ \mathrm{emb}_W(w)$, a natural number $N$ and a complex number $z_1$ such that:

1. $\Psi$ sends linearly independent families to linearly independent families;
2. the moduli lattice of the base of $Z$ is the span of the image under $\Psi$ of the standard lattice;
3. $N$ is a unit in $\mathcal{O}_e(w)$, and $z_1$ is a unit away from $N$;
4. if the theta relation holds for $x$, then the class sum of $\Psi(x)$ is

   $$
   z_1 \nu^{-1} \sum_k \varepsilon(\mathrm{emb}_W(a_k))\, \mathrm{ev}_W(f_k),
   $$

   where $\sum_k a_k f_k$ is the expansion of $x$ and $\nu$ is the scale of the twist.

Lean: `GlobalTheory.PlaceRead.exists_local_component_at_place_alt`.

*Proof.* The embedding $\varepsilon$ extends to an automorphism $\tau$ of $\mathbb{C}$ that fixes the image of $L_0$, since the fields involved are countable and algebraic. The twist chosen through $\tau$ has a good conjugate, and the twisted place has a coefficient map with a scale. The local fixed point of the third layer, from $\mathcal{P}$, gives the integral forms of the twist in conjugated coordinates. The theta lift of a twisted level form is a unit times a class sum. Class sums of conjugate twists have conjugate expansions; this uses the local tuple attached to the discrete series read at the place, which exists by statements 1 to 3. In the Fock model of the [Weil representation](/learn/theta/#the-fock-model), the definite complex forms agree with the twisted complex forms. The product of primes of the tuple at the twisted place is a unit, which gives $N$. The conjugated expansion of the third layer then gives the formula of part 4. $\square$

**Theorem 6.12.4 (Local maps from place data).** Assume statements 1 to 3 and $\mathcal{P}$. With the data of the theorem on the local component at a place, there is a local map at $(w, j + 1)$ for $c$, with a unit $u$, that satisfies the basis, the lattice and the theta conditions.

Lean: `GlobalTheory.PlaceRead.exists_basisAt_latAt_thetaAt_of_atPlace`.

*Proof.* The reading of definite forms is injective on the lattice of integral forms. Choose an extension $\varepsilon$ of $\rho$ and apply the theorem on the local component. The real reading is faithful, and class sums of twisted definite forms are rational, so $\Psi$ descends to a map $e$ to the target space over $\mathrm{emb}_W(w)$. The forms over the chosen field are proportional to their readings, which gives the basis condition. The unit $u$ is the integral unit that comes from the unit $N$ away from the level through the embedding; if the level is trivial we take $u = 1$. Part 4 of the theorem gives the theta condition with this $u$. $\square$

**Theorem 6.12.5 (Local maps at all twisted places).** Assume statements 1 to 3, $\mathcal{P}$ and $\mathcal{S}$, and let $h_L$ be a recursion datum. Then at all stages $x$, for each third level datum $l$ over $x$ and each admissible choice $\mathrm{ch}$ with tied tuple $t_p$, at each twisted place $v$ and each index $i < m$ there is a local map at $(v, i + 1)$ for $\mathrm{ch}$ with a unit $u$.

Lean: `GlobalTheory.PlaceRead.exists_local_map_at_place_alt` (also `GlobalTheory.T.local_component_at_place_determined_alt`, a second name).

*Proof.* Eventually all stages satisfy the host hypotheses and the size bound. Fix $x$, $l$, $\mathrm{ch}$, $v$ and $i$. The rational row of the second level is nonzero at the index, by $\mathcal{S}$. The side condition and the twist condition give the class of $Q$ at the stage. The series character is the inverse of the character $\psi_0$ composed with the embedding. By $\mathcal{P}$, the field condition holds and there is a lambda datum with Teichmüller values. These facts give a real side $X$ with its pins and the place data at $(v, i)$. The theorem on local maps from place data gives the local map. $\square$

**Theorem 6.12.6 (Character data from a choice).** Assume statements 1 to 3, $\mathcal{P}$ and $\mathcal{S}$, and let $h_L$ be a recursion datum. Then at all stages $x$, for each third level datum $l$ over $x$ and each admissible choice $\mathrm{ch}$ with tied tuple $t_p$, there is a height counting character datum $c$ over $l$ with $c_{\mathrm{tw}} = \mathrm{ch}_{\mathrm{tw}}$.

Lean: `GlobalTheory.ChoiceRead.exists_stC_choice_alt` (also `GlobalTheory.T.nonGalois_exists_choice_alt`, a second name).

*Proof.* The theorem on local maps at all twisted places gives, at each twisted place $v$ and each index $i$, a local map $e_{v, i}$ with a unit $u_{v, i}$. Replace $e_{v, i}$ by $u_{v, i}^{-1} e_{v, i}$: its image is now the standard lattice, and the theta condition holds with the unit $1$. With these maps the choice $\mathrm{ch}$ becomes a choice with local maps, and the tuple $t_p$ becomes a tuple with local maps. The side condition and the theta condition of the moduli data hold for the new choice, because they hold at each twisted place. These data form a height counting character datum, and its twist indices are those of $\mathrm{ch}$. $\square$

**Theorem 6.12.7 (Strict henselian acyclic levels).** Assume statements 1 to 3, $\mathcal{P}$ and $\mathcal{S}$, and let $h_L$ be a recursion datum. Then at all stages $x$ of a datum $P$ over a base $B$ with twist datum $T$, for each third level datum $l$ over $x$ and each map $s$ from places to twist indices such that

1. at each place $v$, the index $s(v)$ reads at $v$ for some reading,
2. $s(\bar v) = s(v)$ for each place $v$,

there is a height counting character datum $c$ over $l$, with the weight and the character of $T$, such that $c_{\mathrm{tw}} = s$. So each third level datum extends to a strict henselian acyclic level datum with twist indices $s$.

Lean: `GlobalTheory.LevCmp.stageCExists_of_harishChandra_serN` (also `GlobalTheory.T.stageCExists_of_casselmanWallach`, a second name).

*Proof.* Eight statements hold at all stages together: the theorem on character data from a choice, and seven facts on the twisted places. These say that the good places of the level are the places of the level datum, that the twist conductors avoid the excluded primes, that the bad places lie in the union of the good places and the places of $Q$, that the twisted side readings have the parabolic shape of the Hecke readings, that the level is uniform over the CM datum, that the joint level is good for the twists, and that the cell weights of the side readings are good for the twists. Fix $x$, $l$ and $s$. Since $s(v)$ reads at $v$, the residue characteristic of the twist index $s(v)$ is that of $v$. A comparison choice exists with $\psi$ the character of $T$, $Q$ the place map of $P$, $k$ the weight of $T$ and twist indices $s$; the seven facts show that it is admissible. The theorem on character data from a choice gives $c$ with $c_{\mathrm{tw}} = s$. $\square$

**Remark 6.12.8 (Formalization).** The theorems are at [LevelComparisonChoicesExistAtAllPlaces.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LevelComparisonChoicesExistAtAllPlaces.lean#L107) (second name at line 133), [NonGaloisExistsChoice.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NonGaloisExistsChoice.lean#L19) (line 41) and [LocalComponentAtPlaceDetermined.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LocalComponentAtPlaceDetermined.lean#L36) (lines 94, 166 and 197). The conclusion of the last theorem is `ThirdStageExists` ([ExtensionWithOrigin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExtensionWithOrigin.lean#L37)). The three published statements 1 to 3 are used only once, in the local tuple of the discrete series read at the place, inside the proof of the local component theorem (about line 77); every other theorem of this section passes them on. The name "local component at place determined" does not match its statement, which gives local maps and says nothing on uniqueness. We did not unfold `AtPlace`, `BasisAt`, `LatAt`, `ThetaAt`, `ChoiceSide`, `TwOK`, `ReadsAt` or the character datum, so the definitions above give their roles; the formula in part 4 of the local component theorem follows the statement but omits its coercions.
