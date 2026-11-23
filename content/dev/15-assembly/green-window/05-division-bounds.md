---
title: Division bounds
decls:
  - Formalism.L2.G.ServT.closed_servF_of_servT_of_dGamSize
  - GlobalTheory.Top.closed_family_admissible_twist_link_alt
  - Formalism.L2.DIV.RestAll.bRest_all_alt
  - GlobalTheory.Top.link_brest_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Division bounds

This section proves two of the inputs of the division kernel bound in [the shape theorem](/entry/shape-closed-link-n-of-green/). The first is the valuation bound $\mathrm{adm}_2$ on the working class, from a service bound at the primes. The second is the remaining division bounds: a frame number bound, two rationality conditions and a sign. The shape theorem joins them into the bound $\mathrm{Link}_{\mathrm{DIV}}$ in step 6 of its proof, on the way to [ZeroFreeAll from Green, VWin and HypsAlt](/step/zero-free-all-of-green-v-win/).

We keep the notation of the last section: families $F$ with data $D(x,i)$ and size data $L(x,i)$, the notation $\mathrm{Ev}_F$, and $\mathrm{Closed}(\mathcal{C}, P)$ from [the predicate Closed](/step/closed-def/).

**Definition 3.5.1 (The working class).** Let $\mathcal{A}$ be a family class. A *twist selection* on $\mathcal{A}$ chooses, for each family of $\mathcal{A}$, each $x$ above a threshold and each $i$, a bundle of data at $D(x,i)$. The class $\mathcal{A}'$ adds to $\mathcal{A}$ five conditions on the divisors, the tame places, the boxes and the rows, a bound $C_{YL} \le 9$, a smoothness condition and a twist condition. The *working class* $\mathcal{D}(\mathcal{A})$ adds to $\mathcal{A}'$ three conditions: a chosen datum with constant $3$, the size bound $\mathrm{TuSize}$, and the size bound $\mathrm{DGamSize}$. See [the record HypsAlt](/step/hyps-alt-def/).

**Definition 3.5.2 (Service bounds).** $\mathrm{Serv}(F)$ says: there are $C \ge 0$ and $x_0$ such that for all $x \ge x_0$ with $x > x_1$ and all $i$, three bounds hold for the data at $(x,i)$ with constant $C$: size conditions at the type primes, a bound on a conclusion of the first kind, and a valuation bound on the columns away from the type primes. A twist selection is *served* on $\mathcal{C}$ if two conditions hold. First, a bound on the twisted local systems of each family is closed on $\mathcal{C}$. Second, for each family of $\mathcal{C}$, each $x$ above the threshold of the selection and each $i$, the kernel entry chosen by the selection meets a list of orbit conditions: unit conditions, rational kernel maps, even conditions at inert places, an orbit bound without operator, jet integrality and a shape condition.

**Theorem 3.5.3 (Service from a served selection).** Let $\mathcal{C}$ be a family class with a twist selection. Assume $\mathrm{Closed}(\mathcal{C}, \mathrm{DGamSize})$ and that the selection is served on $\mathcal{C}$. Then $\mathrm{Closed}(\mathcal{C}, \mathrm{Serv})$.

Lean: `Formalism.L2.G.ServT.closed_servF_of_servT_of_dGamSize`

*Proof.* This is [the sum over primes service](/entry/sum-over-primes-service/) applied to the hypotheses of that theorem. Those hypotheses copy the bound on twisted local systems and ask for some kernel entry with the orbit conditions; take the entry chosen by the selection, with its threshold. $\square$

**Definition 3.5.4 (The valuation bound $\mathrm{adm}_2$).** Let $D$ be a datum and $L$ size data. $\mathrm{adm}_2(D, L)$ says: for each word $u$, each place $w$, each vector $\varphi$ of the lattice $L.\mathrm{NuLat}(u)$ and each vector $F$ of the space at $w$ that lies in the base part, the period column value of $(u, \varphi, F)$ is the image of an element $y$ of the number field $L_L$, and either $y = 0$ or $v_w(y) \ge \lfloor \mathrm{ur}(D, w, L.\mathrm{sg}(u,w)) \rfloor$.

**Theorem 3.5.5 (The valuation bound on the working class).** Let $\mathcal{A}$ be a family class with a twist selection that is served on $\mathcal{D}(\mathcal{A})$. Assume that these bounds are closed on $\mathcal{D}(\mathcal{A})$, each eventually in $x$ for $x > x_1$ and each $i$:

1. a sixth conclusion and a Weyl bound on period class sums for $D(x,i)$;
2. a bound on twisted point integrals and an admissibility of twisted periods for the twist of $D(x,i)$;
3. a sharp fifth conclusion and a bound on twisted columns at the type prime, at each word $u$;
4. a constant $C_1$ that bounds the used tuples and the family size at the type prime.

Then $\mathrm{Closed}(\mathcal{D}(\mathcal{A}), F \mapsto \exists x_0, \forall x \ge x_0, x > x_1 \Rightarrow \forall i, \mathrm{adm}_2(D(x,i), L(x,i)))$.

Lean: `GlobalTheory.Top.closed_family_admissible_twist_link_alt`

*Proof.* The proof fills a record of eight closed bounds on $\mathcal{D}(\mathcal{A})$ and applies a lemma on admissibility at generator places. Six fields are the hypotheses. The service bound comes from [service from a served selection](/entry/closed-serv-f-of-serv-t-of-d-gam-size/); the bound $\mathrm{DGamSize}$ holds on $\mathcal{D}(\mathcal{A})$ by the definition of the class. The coprime stabiliser bound at level primes comes from a closed lemma with $C_0 = 3$. The lemma gives $\mathrm{adm}_2$ and a second bound $\mathrm{adm}_{12}$; the proof keeps $\mathrm{adm}_2$. $\square$

**Definition 3.5.6 (The remaining division bounds).** Let $F$ be a family and $C_{\mathrm{abs}}, C_H$ reals. $\mathrm{Rest}(F, C_{\mathrm{abs}}, C_H)$ has four parts:

1. if the complement of $F$ has two elements and $\mathrm{DIV}_N(F)$ holds, then the frame number bound for $F$ with $C_{sz}$ and $C_H$ holds;
2. eventually each $D(x,i)$ is rational: the pairing of two images equals the image of a pairing under the embedding into $L_L$, so it takes values in $L_L$;
3. eventually each $D(x,i)$ is full: the lattice of the realisation is finitely generated and spans its space over $L_L$;
4. eventually $0 \le L(x,i).\mathrm{La}$.

**Theorem 3.5.7 (The remaining division bounds).** Let $\mathcal{A}$ be a family class and $C_{\mathrm{abs}}$ a real. Assume:

1. a twist selection on $\mathcal{A}$ with five companion choices, the last a bundle of indefinite realisations;
2. at each selected point, the realisation has bounded rows, the base-level choice meets the division row and point conditions, and all realisations are primitive;
3. a row condition closed on $\mathcal{D}(\mathcal{A})$;
4. the closed tie condition: eventually each $D(x,i)$ is tied over $\mathbb{R}$ and carries a symmetric tied column datum whose forms meet a finiteness condition.

Then $\mathrm{Closed}(\mathcal{D}(\mathcal{A}), F \mapsto (\mathrm{TuSize}(F) \wedge \mathrm{DGamSize}(F) \Rightarrow \mathrm{Rest}(F, C_{\mathrm{abs}}, C_H)))$.

Lean: `Formalism.L2.DIV.RestAll.bRest_all_alt`

*Proof.* The proof has four steps.

1. A threshold lemma uses the bounded rows, the primitivity, the division row condition and the row condition. It gives a function $C_{F0}$ such that $F$ is large for the threshold, and such that $\mathrm{DIV}_N(F)$ implies, eventually, $\mu_{\max} + \operatorname{mean}_e \log \kappa_R(e) \le x^{C_{F0}} b$.
2. For part 1, fix a family. The tie and $\mathrm{TuSize}$ give the level condition. It gives the rank condition and the full $\nu$ condition. [The concrete $\mathrm{Link}_G$](/entry/link-g-concrete5/) gives $\mathrm{Link}_G$. The bound [from the level](/entry/hh-of-lvl/) joins these with step 1 and a bound on $\mu_{\max}$ from $\mathrm{TuSize}$.
3. A rationality lemma gives parts 2 and 3, from the row condition, the primitivity, the column choice and the division row and point conditions.
4. Part 4 holds for every family.

$\square$

**Theorem 3.5.8 (The remaining division bounds at the constant 2).** Under the hypotheses of the last theorem, $\mathrm{Closed}(\mathcal{D}(\mathcal{A}), F \mapsto (\mathrm{TuSize}(F) \wedge \mathrm{DGamSize}(F) \Rightarrow \mathrm{Rest}(F, 2, C_H)))$.

Lean: `GlobalTheory.Top.link_brest_alt`

*Proof.* This is [the remaining division bounds](/entry/b-rest-all-alt/) applied to $C_{\mathrm{abs}} = 2$. $\square$

**Remark 3.5.9 (Formalization).** The theorems are in GServT.lean (line 31), [ClosedFamilyAdmissibleTwistLink.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ClosedFamilyAdmissibleTwistLink.lean#L12) (line 12), BrestFinalAll.lean (line 25) and LinkBrest.lean (line 18).

- The first theorem is a wrapper of `sum_over_primes_service` through `sumOverPrimesService_of_servT` (GServT.lean line 28). The service file is named after Weil, Jacquet and Shalika, but we have not checked that the service bound states a result of theirs.
- In the second theorem the bound `adm12` is proved and then dropped. Several files define different predicates named `adm2`; the $\mathrm{Adm}_2$ of the last section uses `AuxBlock8.adm2`, not the predicate here.
- The constant $C_{\mathrm{abs}}$ is never used: the structure `RemainingDivisionBounds` (IndefiniteRealisationChoice.lean line 158) takes it as a parameter but no field reads it. It only fixes the type of what the shape theorem builds next, where `toRows_alt` copies the four parts into a bound whose field `pkg` reads the constant.
- Part 4 holds for every family by `la_of` (RecBridgeWire.lean line 16), so it carries no content from the hypotheses.
- We have not unfolded the frame number bound, the division row and point conditions, the row condition, the seven hypotheses of the second theorem, or the three parts of the service bound.
