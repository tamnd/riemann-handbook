---
title: The four tie conditions
decls:
  - GlobalTheory.T.tieChi_at_members_of_depthZero
  - GlobalTheory.TypePrimesFinished.locComp_of_isRc_classMapD_cenLoc
  - GlobalTheory.T.tieChi_at_mem_of_depth_zero_inputs
  - GlobalTheory.HeightCounting.Up.PendLayer.locComp_of_isRc_classMapD_cenLoc
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The four tie conditions

This section proves the four tie conditions $\mathrm{Tie}_4$ at every layer point. Step 2 of [the closed link bound, given a cut](/entry/final-of-alt/) uses them. The four conditions say how the local characters at the type primes are tied to the de Rham data, to the eigenvalues of the central elements, to the inertia and to the labels of the series. The proof gathers facts at each layer point and passes them to [the two tie conditions for one datum](/entry/tie-chi-of-lab-all-green-chi-cen/), which has the content. Part 2 of the chapter treats that result.

**Definition 8.7.1 (Layer points).** Let $h_L$ witness [the local Langlands recursion](/step/rect-exists-def/). A property $P$ holds *at every layer point* for $h_L$ if, eventually in the scale, for each context, base $B$, frame and twist datum with the property $K_{P_x}$, and for each column $w$, index $Z$ and further data (a set of places, a base level, rows $t$, a norm choice and its extension) such that the default extension is nonempty, the real rows of $t$ are nonempty and the column is pinned, $P$ holds. The datum of the point is $D = w.D(Z)$.

Two published inputs enter here, besides the published inputs of the third layer, a record of fourteen named results.

**Definition 8.7.2 (Depth zero support).** *Depth zero support* says: let $k$ be a local field with ring of integers $O$, and let $K_1$ be the kernel of $\mathrm{GL}_n(O) \to \mathrm{GL}_n$ of the residue field. If an irreducible representation $\pi$ of $\mathrm{GL}_n(k)$ has a nonzero vector fixed by $K_1$, then so does each member of its cuspidal support.

This has the form of a result of Moy and Prasad on representations of depth zero (Comment. Math. Helv. 71, 1996). The *height continuity* input is a continuity condition on the representations of the Weil-Deligne sides.

**Definition 8.7.3 (The four tie conditions).** Let $D$ be a datum, with type primes $\ell_i = g_k$. The *four tie conditions* $\mathrm{Tie}_4(D)$ are:

1. the *character tie*: at each type prime and each place $v$ there is $u \in \{\chi_J, \chi_J^{-1}\}$ such that the local character at $i$ is de Rham at the place $w$ over $v$ and at its conjugate place, with item polynomial $X - u$ at $w$ and $X - u^{-1}$ at the conjugate;
2. the *pending tie*: there is a pending datum $P$ of $D$ that is admissible in depth zero and has the *eigen span* property: if a central element $z$ acts by a scalar $c$ on the types at $x$, then $z$ acts by $c$ on the Hecke eigenvectors at $x$;
3. the *inertia tie*: for a potentially crystalline local representation, the inertia polynomial of its Weil-Deligne representation kills $D_{\mathrm{pcris}}$;
4. the *series tie*: if the local operator of a series label $f$ acts by a nonzero map on a module of the parameter $\sigma'$, then $f$ is the label of $\sigma'$ at $v$.

The ties link the local [[Galois representation|JQEYEQJY2G]] at a type prime to the type of the [[local Langlands|9E45NBX1G0]] parameter. The de Rham and crystalline notions are those of [period rings](/learn/galois-representations/#period-rings).

**Proposition 8.7.4 (The first two ties at layer points).** Assume height continuity, the published inputs of the third layer and depth zero support. Let $h_L$ be as above. Then at every layer point for $h_L$, the datum $D$ satisfies the character tie and the pending tie.

Lean: `GlobalTheory.HeightCounting.Up.PendLayer.locComp_of_isRc_classMapD_cenLoc` (also `GlobalTheory.T.tieChi_at_mem_of_depth_zero_inputs`, a second name).

*Proof.* There are two steps.

1. **Four facts at each layer point.** Properties that hold at every layer point join. The following four hold.
   - The central elements of the family $M$ of the point are local, stable under the $\mathbb{Z}_\ell$ structure and integral.
   - Height continuity gives the count of the jumps.
   - The published inputs give a tied pair $X$: a character choice datum $X.P$ of $D$ and a real datum that agrees with it. The datum $X.P$ is pinned at the point. That is, it has the character frame, the norm choice, the tuple, the representations and the family $M$ of the point, and it satisfies the label conditions, the green label condition and the character condition.
   - Seven size and host facts hold at each record, and they move to layer points since the column is pinned. Of these, the bound on the roots in the coefficient field is used.
2. **The ties.** At each point, apply [the two tie conditions for one datum](/entry/tie-chi-of-lab-all-green-chi-cen/) to $X.P$ and the facts of step 1. The pin gives $X.P.M = M$, so the central elements of $M$ are local for $X.P.M$. $\square$

**Theorem 8.7.5 (The four ties at layer points).** Assume height continuity, the published inputs of the third layer and depth zero support. Let $h_L$ be as above. Then at every layer point for $h_L$, the datum $D$ satisfies $\mathrm{Tie}_4(D)$.

Lean: `GlobalTheory.TypePrimesFinished.locComp_of_isRc_classMapD_cenLoc` (also `GlobalTheory.T.tieChi_at_members_of_depthZero`, a second name).

*Proof.* At each layer point join three facts.

1. The Proposition (The first two ties at layer points) gives the character tie and the pending tie.
2. The published inputs of the third layer give a character choice $P$ of $D$ at each layer point. The inertia tie follows from the existence of a character choice.
3. The published inputs of the third layer give the series tie at each layer point. $\square$

Height continuity and depth zero support enter only through the Proposition. The published inputs of the third layer give the other two ties directly.

**Remark 8.7.6 (Formalization).** The theorem and its second name are at [LocalTypeDeterminedAtAllPrimes.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LocalTypeDeterminedAtAllPrimes.lean#L22), lines 22 and 36, and the proposition and its second name at [PendingLayerConditionAtMember.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PendingLayerConditionAtMember.lean#L46), lines 46 and 62. The second names are `first | exact … | …` tactics. The inputs are `HtCard`, `PublishedInputsThirdLayerAlt` and `DepthZeroSupport`, and the ties are `tieChi`, `admDZ` with `EigSpan`, `TieInePoly` and `SerLoc`. In the theorem, step 2 is `exists_character_choice_pin_at_of_third_layer`, which gives a pin that is never used, then `tieInePoly_of_characterChoice`; step 3 is `serLoc_at_member_of_published_inputs`. In the proposition, step 1 joins `cenLoc_zlStable_cenInt_at_members`, `jumpsCard_at_members_of_htCard`, `isTied_of_layer_member_alt` and `sizes_host_at_record` with `atMem_and'`, and only the fact `RootsLL` of the last one is used. The short name `locComp_of_isRc_classMapD_cenLoc` names theorems in 21 files of the Lean tree with other statements, in namespaces such as `PendLayer`, `TypePrimesFinished`, `PinClose`, `TieChiPin` and `SerFinished`; nothing called `isRc` or `classMapD` occurs here. The name `tieChi_at_members_of_depthZero` names only the first of four ties. We did not check that the form of `DepthZeroSupport` with $K_1$ is the statement of Moy and Prasad.
