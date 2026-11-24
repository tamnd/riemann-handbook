---
title: Depth zero types and the block split
decls:
  - GlobalTheory.BlockTypeSplit.block_type_split_local_alt
  - GlobalTheory.BlockTypeSplit.locComp_of_isRc_classMapD_cenLoc
  - GlobalTheory.T.splitLoc_of_greenLab_depth_zero
  - GlobalTheory.DepthZeroRow.locComp_of_isRc_classMapD_cenLoc
  - GlobalTheory.T.admDepthZero_of_rowMod_labAll_greenLab
  - GlobalTheory.CenAtLoc.cen_loc_zl_stable_cen_int
  - GlobalTheory.T.cenLoc_zlStable_cenInt_at_members
  - GlobalTheory.T.cenLoc_at_members
  - GlobalTheory.PinClose.locComp_of_isRc_classMapD_cenLoc
  - GlobalTheory.HeightCounting.Up.PendLayer.tieChi_of_labAll_green_chi_cen
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Depth zero types and the block split

This section proves [the two tie conditions for one datum](/entry/tie-chi-of-lab-all-green-chi-cen/), which step 2 of the Proposition (The first two ties at layer points) of Section 7 uses. These are the character tie and the pending tie of $\mathrm{Tie}_4$. The local core is a statement on [representations of depth zero](/learn/representations/#depth-zero-representations-and-types) of $\mathrm{GL}_{r+t}$ over a $p$-adic field: a vector of a block type splits the representation as a product of a representation of $\mathrm{GL}_r$ and an unramified twist of a spherical representation of $\mathrm{GL}_t$. From it we read the [[local Langlands|9E45NBX1G0]] parameter at the places over the type primes. That gives the admissibility in depth zero, and the pending tie follows.

We keep the notation of Section 7. A datum $D$ has a CM field $E$, type primes $g_0$ and $g_1$, ranks $r$, $t$ and $n_V = r + t$, local indices $i$ with primes $\ell_i$, and points $\Pi$ at $i$ with local parameters $\mathrm{loc}_i(\Pi, w)$ at the places $w$ of $E$. For $k \in \{0, 1\}$ and a place $v$ in the set of places of $D$ over $g_k$, the datum fixes a place $w_v$ of $E$ over $v$, and a character $\chi_J = \chi_J(i, k, v)$ of $\mathbb{F}_{g_k}^\times$. Each local parameter has an *item polynomial* $\mathrm{items}(w, \cdot) \in \mathbb{F}_{g_k}[X]$, and it is *of monodromy zero* if its Weil-Deligne representation has $N = 0$.

**Definition 8.12.1 (Labels and block vectors).** Let $F$ be a nonarchimedean local field with ring of integers $O$, maximal ideal $\mathfrak{m}$ and residue field $\mathbb{F}_p$. A *label datum* $L$ for $p$ assigns to a class function of $\mathrm{GL}_r(\mathbb{F}_p)$ a polynomial $f \in \mathbb{F}_p[X]$, its *label*, and to a character $\theta$ of $\mathbb{F}_p^\times$ a value $u \in \mathbb{F}_p$. A smooth character $\chi$ of $F^\times$ is *tame* if it is trivial on $1 + \mathfrak{m}$; it *lifts* $\theta$ if $\chi(x) = \theta(a)$ for each unit $x \equiv a \bmod \mathfrak{m}$. Let $\pi$ be a smooth representation of $\mathrm{GL}_{r+t}(F)$ and $\chi$ tame. A *block vector* for $\chi$ is a vector $x$ with

$$\pi(h)x = \chi(\det h_{22})\, x$$

for each $h \in \mathrm{GL}_{r+t}(O)$ whose lower left $t \times r$ block is $0$ mod $\mathfrak{m}$ and whose upper left $r \times r$ block is $1$ mod $\mathfrak{m}$. Here $h_{22}$ is the lower right $t \times t$ block. For a simple representation $\rho$ of $\mathrm{GL}_r(\mathbb{F}_p)$ let $e_\rho$ be its central idempotent, acting through the reduction of the upper left block. We say $e_\rho$ does not kill $x$ if $e_\rho x \ne 0$.

The label plays the role of Green's parametrization of the irreducible characters of $\mathrm{GL}_r(\mathbb{F}_p)$ by polynomials over $\mathbb{F}_p$ (Green 1955). A block vector is fixed by a parahoric subgroup up to the character $\chi \circ \det$ on the lower block, so it belongs to a depth zero type in the sense of Moy and Prasad.

We take the following local results as given. *Bernstein-Zelevinsky finiteness* and *the geometric lemma* are the finiteness of [the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module) and its filtration by double cosets (Bernstein and Zelevinsky 1977, Section 2). The *irreducibility of unlinked products* is the theorem of Zelevinsky that a product of unlinked segments is irreducible (Zelevinsky 1980, Theorem 9.7). The *injectivity of the depth zero Jacquet functor* is a statement in the form of Moy and Prasad (1996):  taking $K_1$-invariants is compatible with the Jacquet module. These four, with eleven more, form the record of *local theta inputs*.

**Theorem 8.12.2 (The block split).** Assume the local theta inputs. Let $F$ be a nonarchimedean local field with residue field $\mathbb{F}_p$, $L$ a label datum for $p$, $\chi$ a tame smooth character of $F^\times$ that lifts $\theta$, and let $L$ give the value $u$ to $\theta$. Let $\pi$ be an irreducible representation of $\mathrm{GL}_{r+t}(F)$ and $\rho$ a simple representation of $\mathrm{GL}_r(\mathbb{F}_p)$ with label $f$ and $f(u) \neq 0$. Let $x$ be a block vector for $\chi$ that $e_\rho$ does not kill. Then there are irreducible $\pi_1$ of $\mathrm{GL}_r(F)$ and $\pi_2$ of $\mathrm{GL}_t(F)$ with $\pi_2$ spherical and

$$\pi \cong \pi_1 \times (\pi_2 \otimes \chi \circ \det),$$

and $\pi_1$ has a $K_1$-fixed vector that $e_\rho$ does not kill.

Lean: `GlobalTheory.BlockTypeSplit.block_type_split_local_alt`.

*Proof.* There are four steps.

1. **A parahoric vector.** The idempotent $e_\rho$ and the block vector give a nonzero vector fixed by the parahoric of the block shape $(r, t)$, up to the character $\rho \otimes \chi \circ \det$.
2. **Cuspidal support.** By the injectivity of the depth zero Jacquet functor, this vector survives in the Jacquet module for the parabolic of shape $(r, t)$. So $\pi$ is a subquotient of a product of cuspidal representations of depth zero. Bernstein-Zelevinsky finiteness, the geometric lemma and the irreducibility of unlinked products show that the support has at most $t$ factors of the form $\chi \cdot \mu$ with $\mu$ unramified of $\mathrm{GL}_1$.
3. **Exactly $t$ factors.** If there are fewer than $t$ such factors, then by the geometric lemma the part of the vector on the $\mathrm{GL}_r$ block involves $\chi$, and $u$ is a root of the label $f$ of $\rho$. This contradicts $f(u) \ne 0$.
4. **The split.** With exactly $t$ factors $\chi\mu_1, \dots, \chi\mu_t$, the irreducible $\pi$ is the product of the irreducible $\pi_1$ with the other factors and of the spherical $\pi_2 \otimes \chi \circ \det$ with these $t$ factors. The image of the vector in the $\mathrm{GL}_r$ cell of the Jacquet module is a $K_1$-fixed vector of $\pi_1$ that $e_\rho$ does not kill. $\square$

Now the global form. A *group side* $\Gamma$ of $D$ gives, for each $k$ and each $d$, a label datum at $g_k$ for the representations of $\mathrm{GL}_d(\mathbb{F}_{g_k})$. It satisfies the *Green label condition* if each simple cuspidal representation $\tau$ of $\mathrm{GL}_d(\mathbb{F}_{g_k})$, $d \ge 1$, has its Green cusp label.

**Corollary 8.12.3 (The block split at the type primes).** Assume the local theta inputs. Let $h_L$ witness [the local Langlands recursion](/step/rect-exists-def/), let $D$ be a datum and $\Gamma$ a group side with the Green label condition. Let $k \in \{0,1\}$, $v$ a place over $g_k$ and $E_w$ the completion at $w = w_v$. Let $\chi$ be a tame smooth character of $E_w^\times$ whose local label is $X - u$, let $\pi$ be irreducible of $\mathrm{GL}_{r+t}(E_w)$, and let $\rho$ be in the series of label $f$ with $f(u) \ne 0$. If $\pi$ has a block vector for $\chi$ that $e_\rho$ does not kill, then the conclusion of the Theorem (The block split) holds for $\pi$.

Lean: `GlobalTheory.BlockTypeSplit.locComp_of_isRc_classMapD_cenLoc` (also `GlobalTheory.T.splitLoc_of_greenLab_depth_zero`, a second name).

*Proof.* The residue field of $E_w$ has $g_k$ elements, since $w$ is split over a place of degree one. The local Langlands recursion at $w$ shows that a tame character with label $X - u$ lifts a character $\theta$ of $\mathbb{F}_{g_k}^\times$ to which the label datum of $\Gamma$ gives $u$; this is local-global compatibility for the CM datum. The Green label condition gives the label $f$ of $\rho$. Now apply the Theorem (The block split). $\square$

**Definition 8.12.4 (Admissible in depth zero).** Let $D$ be a datum. The datum is *admissible in depth zero* if the following holds for all $i$, $k$, $v$, points $\Pi$ at $i$, simple representations $\rho$ of $\mathrm{GL}_r(\mathbb{F}_{g_k})$ and $f \in \mathbb{F}_{g_k}[X]$. Assume $e_\rho$ lies in the series idempotent of $f$, $e_\rho$ occurs at $(i, \Pi, k, v)$, $f$ is squarefree and $f(u) \neq 0$ for $u = \chi_J^{\pm 1}$. Then there is $u \in \{\chi_J, \chi_J^{-1}\}$ such that

$$\begin{aligned} &\mathrm{loc}_i(\Pi, w_v) \text{ has monodromy zero and } \mathrm{items}(w_v) = f\,(X - u)^t, \\ &\mathrm{loc}_i(\Pi, w') \text{ has monodromy zero, } \deg \mathrm{items}(w') = n_V \text{ for each conjugate } w', \end{aligned}$$

and the roots of $\mathrm{items}(w')$ are the inverses of the roots of $f\,(X-u)^t$.

So the type that occurs fixes the local parameter at $w_v$: a regular part with label $f$ and $t$ copies of a tame character. The conjugate place gives the dual, as for a unitary group.

The global hypotheses on a character choice $P$ of $D$ are these. The *label condition* says that at each place $w$ over $g_k$ the item polynomial of each local parameter is the Weil-Deligne label of its parameter. The *character condition* says that the local character of $P$ is good. The *central locality* of a family $M$ says: at each $i$ there is a block lift $L$ of the type group $G_0$ to $\mathrm{GL}_{n_V}(\mathbb{A}_f)$, and central elements $z$ of $\mathbb{C}[G_0]$ act on $M$ through $L$.

**Proposition 8.12.5 (Admissibility in depth zero).** Assume the local theta inputs. Let $h_L$ be as above, $D$ a datum and $P$ a character choice of $D$ with row modules at each $i$. Assume the label condition, central locality of the family of $P$, the Green label condition of the group side of $P$ and the character condition. Then $D$ is admissible in depth zero.

Lean: `GlobalTheory.DepthZeroRow.locComp_of_isRc_classMapD_cenLoc` (also `GlobalTheory.T.admDepthZero_of_rowMod_labAll_greenLab`, a second name).

*Proof.* There are five steps.

1. **A reading.** The finiteness of automorphic forms on $\mathrm{GL}$ and the row modules give a true reading $S$ of $P$: at each split place $w$ an irreducible local representation for each point, whose Weil-Deligne representation under $h_L$ is the local parameter.
2. **The local condition.** The Corollary (The block split at the type primes) and its regular analogue for $\mathrm{GL}_r$ give: if $\pi$ has a block vector for a tame $\chi$ with label $X - u$ that $e_\rho$ does not kill, $f$ squarefree and $f(u) \ne 0$, then the parameter of $\pi$ has monodromy zero and label $f\,(X-u)^t$. For the regular part, a $K_1$-fixed vector not killed by $e_\rho$ with squarefree $f$ gives monodromy zero and label $f$. The spherical twist adds $(X-u)^t$.
3. **Block vectors.** The place $w_v$ is split. If $e_\rho$ occurs at $(i, \Pi, k, v)$, central locality gives a block vector in the local representation of $\Pi$ at $w_v$ that $e_\rho$ does not kill.
4. **The character.** The character condition gives a tame character $\chi$ at $w_v$ with label $X - u$ for some $u \in \{\chi_J, \chi_J^{-1}\}$. Step 2 gives the claim at $w_v$, and the label condition identifies the label with the item polynomial.
5. **The conjugate places.** The label condition gives the conjugate duality of the parameters, so at a conjugate $w'$ the parameter is dual. It has monodromy zero, degree $n_V$ and inverse roots. $\square$

Central locality and two lattice conditions hold at every layer point. The *$\mathbb{Z}_\ell$ stability* says that central elements of the group algebra over the coefficient ring $L_\ell$ keep the lattice of $M$, and *central integrality* says the same for central elements of $\mathbb{Z}[G_0]$ and the integral lattice.

**Proposition 8.12.6 (Central elements at layer points).** Let $h_L$ be as above. At every layer point for $h_L$, central locality of the family $M$ of the point, $\mathbb{Z}_\ell$ stability and central integrality hold.

Lean: `GlobalTheory.CenAtLoc.cen_loc_zl_stable_cen_int` (also `GlobalTheory.T.cenLoc_zlStable_cenInt_at_members`, a second name), `GlobalTheory.T.cenLoc_at_members`.

*Proof.* Properties at every layer point join. Central locality comes from four facts at each point: central elements act rationally, their action is read through the frame, the frame of the tuple agrees with $\mu$, and an adjoint datum exists. Together they give the block lift $L$ and the action through it. The two lattice conditions hold at each point by the integrality of the action of $\mathbb{Z}[G_0]$ on the lattices of the point. $\square$

**Theorem 8.12.7 (The pending datum).** Assume the local theta inputs and depth zero support. Let $h_L$, $D$ and $P$ be as in the Proposition (Admissibility in depth zero), with its four hypotheses. Assume the tie at $0$, the fifth admissibility condition, $\mathbb{Z}_\ell$ stability, central integrality, the series label condition and roots of unity in the coefficient rings. Then there is a pending datum of $D$ that is admissible in depth zero and has the eigen span property.

Lean: `GlobalTheory.PinClose.locComp_of_isRc_classMapD_cenLoc`.

*Proof.* There are four steps.

1. The label condition splits into three ties: inertia, depth and genericity.
2. Central locality shows that the centre of the group algebra keeps the type spaces at the localizations.
3. The label condition, the character condition and depth zero support show that the local parameters are tame at the places over $g_0$ and $g_1$. Depth zero support enters only here.
4. The Proposition (Admissibility in depth zero) gives admissibility. The parameters of the type side are in bijection with the parameters of $D$. A general construction of pending objects from the facts of steps 1 to 3, the tie at $0$, the fifth admissibility condition, the lattice conditions, the series label, the roots of unity and admissibility gives the pending datum with the eigen span property. $\square$

**Theorem 8.12.8 (The two tie conditions for one datum).** Assume the published inputs of the third layer and depth zero support. Let $D$ be a datum and $P$ a character choice of $D$, with a real datum that agrees with it. Assume the count of jumps, the label condition, the Green label condition, the character condition, central locality of the family of $P$, $\mathbb{Z}_\ell$ stability, central integrality and the bound on the roots in the coefficient field. Then $D$ satisfies the character tie, and there is a pending datum of $D$ that is admissible in depth zero with the eigen span property.

Lean: `GlobalTheory.HeightCounting.Up.PendLayer.tieChi_of_labAll_green_chi_cen`.

*Proof.* The decay and the convergence inputs of the third layer give a row module at each $i$ from the agreeing real datum. The local theta inputs, which are part of the third layer inputs, and the count of jumps give the tie at $0$ and the fifth admissibility condition. The bound on roots gives the roots of unity and the rationality of the series idempotents. The character tie follows from the row modules, the label condition and the character condition, by the local-global compatibility of the tame character. The pending datum is the Theorem (The pending datum). $\square$

**Remark 8.12.9 (Formalization).** The theorems are at [NonGaloisBlockTypeSplit.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NonGaloisBlockTypeSplit.lean#L23) (lines 23, 114, 134), [NonGaloisDepthZeroEntrywise.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/NonGaloisDepthZeroEntrywise.lean#L24) (lines 24, 74), [ZlStableAt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ZlStableAt.lean#L23), [ExistsAdStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsAdStatement.lean#L16), [ImportsTerSide.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ImportsTerSide.lean#L18) and [PendingLayerConditionAtMember.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PendingLayerConditionAtMember.lean#L31). The local theta inputs are `ThetaLocalInputsAlt`, with fifteen fields; the block split uses only `bz`, `geo`, `unl` and `mp`, and the other eleven, such as `bern` and `js`, are not used there. We did not unfold these inputs, so the classical forms above are their names, not checked statements. The label datum is `LabelDatum`, and we did not check that its labels are Green's. The second name `splitLoc_of_greenLab_depth_zero` speaks of depth zero, but its statement is the block split `SplitLocalCondition`. The name `admDepthZero_of_rowMod_labAll_greenLab` does not mention central locality `CenLoc`, which step 3 uses. `cenLoc_at_members` wraps `GlobalTheory.CenLocAt.cenLoc_at_member` in [ExistsAd.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsAd.lean#L24), whose module name does not match its statement. The proposition on central elements has no hypotheses. In the last theorem the character tie is `TieChiPin.locComp_of_isRc_classMapD_cenLoc` and the tie at $0$ comes from `a_close_main`. Three theorems of this section share the short name `locComp_of_isRc_classMapD_cenLoc`, as noted in Section 7.
