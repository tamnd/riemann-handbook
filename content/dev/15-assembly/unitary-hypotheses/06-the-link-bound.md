---
title: The link bound
decls:
  - UpperTheory.GalC.final_alt_alt
  - UpperTheory.GalC.final_of_alt
  - UpperTheory.GalC.linkedAt_linkN_of_boundAtTwoThree
  - UpperTheory.GalC.linkN_of_boundAtTwoThree_slot
  - UpperTheory.GalC.linkN_of_twGood_galoisPreconditions
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The link bound

This section proves the norm row $\mathrm{Linked}_p(\mathrm{NRow}(\cdot, \cdot, N_L))$ of Section 1. Step 4 of [the main theorem](/entry/hypotheses-nonempty-of-unramified-exponents-alt/) uses it. The norm row is a closed bound for the link inequality, a bound for a weighted sum of congruence valuations at the twisted places of each datum of a family. We prove it top down. First we reduce the linked form to a slot form, then the slot form to one family. For one family we cut each datum to its good points, prove the bound for the cut family, and move it back. The bound for a cut family is [the closing bound](/entry/concl-f-of-family-facts-and-bound-at-two-three/) of Section 8, and the inputs at each datum are the four tie conditions of Section 7 and the extra bound of Section 10.

**Definition 8.6.1 (Published local inputs).** The *published local inputs* are a record of seven named results: Fontaine's ring $B_{\mathrm{cris}}$, global Artin reciprocity of Section 4, a [local Bloch-Kato](/learn/padic-hodge/#local-bloch-kato-theory) input, an integrality input of Bhatt and Scholze, and three facts of [local Galois cohomology](/learn/galois-cohomology/#local-fields): Tate duality, the Euler characteristic formula and finiteness.

A family $F$ has a threshold $x_1 > 1$ and, for each $x$ and each index $i \in I_x$, a datum $D_{x,i}$ with size data $L_{x,i}$ and, for $x > x_1$, a norm choice $n_{x,i}$. The *Galois preconditions* at a datum and a norm choice are eighteen conditions on the local Galois data. The *four tie conditions* $\mathrm{Tie}_4(D)$ are stated in Section 7.

**Definition 8.6.2 (The link inequality).** Let $F$ be a family. The *link inequality* $\mathrm{LinkN}(F)$ says: there are $C$ and $x_0$ such that for each $x \ge x_0$, each $i \in I_x$ at which the Tate-Shafarevich group is finite of odd order, and each lift $j$ of $D_{x,i}$, if the series $\sum_l v(l)$ converges, then

$$\eta_j(L_{x,i}) \le d_0(j) \Bigl( C \bigl( f m b \Lambda^2 + (\log x)^2 N_c \bigr) + \sum_l v(l) \Bigr).$$

Here $\eta_j$ is the weighted sum of the congruence valuations over the twisted places in the support, $d_0(j)$ is the degree of the lift, $f$ and $m$ are numbers of the datum, $b$, $\Lambda$ and $N_c$ are numbers of the size data, and $v(l) = \log l \sum_{e=1}^{t-1} \mathrm{sha}(l, e)$ for a prime $l$, with $\mathrm{sha}(l, e)$ the length of the $l$-part of a [Selmer and Tate-Shafarevich group](/learn/galois-cohomology/#selmer-and-tate-shafarevich-groups).

**Definition 8.6.3 (Good cuts).** A *cut* $c$ of a datum $D$ keeps some local indices and, at each kept index $i$, a nonempty set $X_i$ of points. Let $Z_i$ be the points at $i$ and $Z^{\mathrm{good}}_i$ the good ones. The cut is *good* if $i$ is kept exactly when $Z^{\mathrm{good}}_i \neq \emptyset$, if $Z^{\mathrm{good}}_i \subseteq X_i$, if the points of $Z_i \cap X_i$ are good, and if a Hecke equivariant endomorphism acts on eigenvectors by a fixed nonzero integer at good points and by $0$ outside $X_i$. The *cut hypothesis* says: each datum $D$ with a norm choice $n$ that satisfies the Galois preconditions and $\mathrm{Tie}_4(D)$ has a good cut, and the cut datum satisfies the facts of a norm choice and $\mathrm{Tie}_4$.

**Theorem 8.6.4 (The link inequality for one family).** Assume the published local inputs and the cut hypothesis. Let $F$ be a family with good twists eventually. Assume that for each $x > x_1$ and each $i$, the datum $D_{x,i}$ and $n_{x,i}$ satisfy the Galois preconditions and $\mathrm{Tie}_4(D_{x,i})$. Then $\mathrm{LinkN}(F)$ holds.

Lean: `UpperTheory.GalC.linkN_of_twGood_galoisPreconditions`.

*Proof.* There are five steps.

1. **Extra bound.** [The extra bound](/entry/exists-const-tie-chi-bound-of-facts/) of Section 10 gives $C \ge 0$ and $C_T \in \mathbb{N}$ such that the facts of a norm choice and $\mathrm{Tie}_4$ at a datum give the extra bound at $C$ and $C_T$.
2. **Cuts.** For $x > x_1$ and each $i$, the cut hypothesis gives a good cut $c_{x,i}$ of $D_{x,i}$. For $x \le x_1$ take the cut that keeps all indices and all points.
3. **The cut family.** Let $F'$ be the family with each datum replaced by its cut. By steps 1 and 2, the facts of a norm choice, $\mathrm{Tie}_4$ and the extra bound hold along $F'$. The cut family has good twists, since $F$ has them.
4. **The bound for $F'$.** [The closing bound](/entry/concl-f-of-family-facts-and-bound-at-two-three/) of Section 8 gives the closing conclusion for $F'$, with the bound at $2$ and $3$ for $F'$ proved from the published local inputs. The local bounds of the closing conclusion give $\mathrm{LinkN}(F')$.
5. **Back to $F$.** $\mathrm{LinkN}$ moves from $F'$ to $F$. For $x > x_1$ this needs the good cut, the bound of the multiplicity of a good point by the rank, and the third admissibility condition, which is one of the Galois preconditions. The new constant is $C + C_1$, where $C_1$ bounds the logarithm of the integer of the cut, uniformly in the family. $\square$

Now we pass from one family to a slot. A selection $\sigma$ at a slot $Q$ and a linkage $\Lambda$ selects bundles, and each bundle carries a datum and a norm choice. Let $\mathrm{GP}$ be the property of bundles: the datum and its norm choice satisfy the Galois preconditions and $\mathrm{Tie}_4$.

**Proposition 8.6.5 (The link inequality at a slot).** Assume the published local inputs and the cut hypothesis. Let $Q$ be a slot and $\Lambda$ a linkage. Assume that eventually each bundle at a point of $Q$ that $\Lambda$ links has $\mathrm{GP}$, and that $\mathrm{NRow}(Q, \Lambda, B_{23})$ holds. Then $\mathrm{NRow}(Q, \Lambda, N_L)$ holds.

Lean: `UpperTheory.GalC.linkN_of_boundAtTwoThree_slot`.

*Proof.* The first hypothesis is a row whose statement says that every bundle that $\sigma$ selects has $\mathrm{GP}$. Join it with the second hypothesis, and fix a class $\mathcal{A}$ and a selection $\sigma$. The second hypothesis gives $\varepsilon_1 > 0$ and, for each $\varepsilon \in (0, \varepsilon_1]$, a threshold $K$. Keep $\varepsilon_1$ and $K$. Let $F$ be a family in $\mathcal{D}_3(\mathcal{A})$ that is large for $K$. Then $F$ has good twists and $F$ is in $\mathcal{A}$, so the Galois preconditions and $\mathrm{Tie}_4$ hold at each datum of $F$. The Theorem (The link inequality for one family) gives $\mathrm{LinkN}(F)$. $\square$

The proof uses only the numbers $\varepsilon_1$ and $K$ of $B_{23}$, not the bound at $2$ and $3$ itself. The bound at $2$ and $3$ is proved again inside step 4 of the theorem.

**Corollary 8.6.6 (The linked link inequality).** Assume the published local inputs and the cut hypothesis, and let $p$ be a parameter set. Assume that $\mathrm{GP}$ holds eventually at the linked bundles in linked form at $p$, and that $\mathrm{Linked}_p(\mathrm{NRow}(\cdot, \cdot, B_{23}))$ holds. Then $\mathrm{Linked}_p(\mathrm{NRow}(\cdot, \cdot, N_L))$ holds.

Lean: `UpperTheory.GalC.linkedAt_linkN_of_boundAtTwoThree`.

*Proof.* Let $R_1$ and $R_2$ be the slots of the two hypotheses. The large base conditions for $R_1$ and $R_2$ give the large base condition for $R_1 \wedge R_2$. The slot $Q'_p \wedge R_1 \wedge R_2$ is smaller than $Q'_p \wedge R_1$ and than $Q'_p \wedge R_2$. An eventual property and a row at a slot hold at each smaller slot. Now apply the Proposition (The link inequality at a slot) to $Q'_p \wedge R_1 \wedge R_2$ and $\Lambda_p$. $\square$

**Theorem 8.6.7 (The closed link bound, given a cut).** Assume the published local inputs, the cut hypothesis, the published inputs of the third layer, the geometric compatibility of the [[Galois representation|JQEYEQJY2G]]s and the depth zero support. Let $h_L$ witness [the local Langlands recursion](/step/rect-exists-def/), let $c \in \mathbb{R}$ and let $p = p(h_L, c)$. Assume:

1. at every layer point, the datum and its norm choice satisfy the Galois preconditions;
2. $\mathrm{Linked}_p(\mathrm{NRow}(\cdot, \cdot, B_{23}))$.

Then $\mathrm{Linked}_p(\mathrm{NRow}(\cdot, \cdot, N_L))$ holds.

Lean: `UpperTheory.GalC.final_of_alt`.

*Proof.* There are four steps.

1. **Witnesses move.** The slots of $p$ move positions along the extension with list and the closure of the trivial geometry, so witnesses pass along the slots.
2. **Ties.** At every layer point, [the four tie conditions](/entry/tie-chi-at-members-of-depth-zero/) of Section 7 hold. They come from the height part of the compatibility record, the published inputs of the third layer and the depth zero support.
3. **A linked row.** Join hypothesis 1 and step 2. A property of a datum and its norm choice that holds at every layer point gives an eventual property in linked form at $p$, by step 1. Here an element of the extension with list gives an element of the extension with law by the first projection. So $\mathrm{GP}$ holds in linked form at $p$.
4. **Conclusion.** The Corollary (The linked link inequality) applies to step 3 and hypothesis 2. $\square$

**Theorem 8.6.8 (The closed link bound).** Assume the published local inputs, the published inputs of the third layer, the geometric compatibility of the Galois representations, the local Selmer input, the depth zero support, local finiteness, local Tate duality and the local Euler characteristic. Let $h_L$ and $c$ be as above, and $p = p(h_L, c)$. If $\mathrm{Linked}_p(\mathrm{NRow}(\cdot, \cdot, B_{23}))$ holds, then $\mathrm{Linked}_p(\mathrm{NRow}(\cdot, \cdot, N_L))$ holds.

Lean: `UpperTheory.GalC.final_alt_alt`.

*Proof.* This is the Theorem (The closed link bound, given a cut) applied to two facts. [The good cut facts](/entry/exists-good-cut-facts-tie4/) give the cut hypothesis, from the Chebotarev part of the third layer inputs and the three local facts. [The Galois preconditions at layer points](/entry/galois-preconditions-at-mem/) give hypothesis 1, from the third layer inputs, the compatibility, the local Selmer input and the three local facts. $\square$

**Remark 8.6.9 (Formalization).** The four lower results are in [LinkNFam.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean#L37), at lines 37, 54, 64 and 75, and the top one at [CFinal.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CFinal.lean#L19), whose type is the abbreviation `NLink.Final.mainTheorem`. The published local inputs are `Hypotheses₂`, the cut hypothesis is `CutGivesAlt` (line 35), and $\mathrm{GP}$ is `GaloisPreconditions` with `Tie4`. The hypothesis $B_{23}$ is redundant twice. In `linkN_of_boundAtTwoThree_slot` only $\varepsilon_1$ and $K$ of `h23` are used, and its bound `hK` and the largeness hypothesis are dropped ([lines 61 to 63](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean#L61)); the bound is proved again by `at23_family_alt hP` at [line 51](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean#L51). Also `boundAtTwoThree_linked_of_recT` in [At23OfAll.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/At23OfAll.lean#L24) proves the linked $B_{23}$ from `Hypotheses₂`. The names "of bound at two three" suggest the opposite. The cut for $x \le x_1$ is `CutD.all`, an unused placeholder. Step 1 of the last proof but one is `slot_mv_extension_with_list_geo_cl` with `witnesses_pass_along_set_division`, and step 3 is `AtMem.and_z` with `atMem_at_wit_alt`. The local facts without the suffix K, in `GalCoh.lean`, are other definitions than those of `Hypotheses₂`, and we did not compare them.
