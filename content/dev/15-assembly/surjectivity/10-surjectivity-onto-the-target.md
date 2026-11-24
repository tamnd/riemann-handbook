---
title: Surjectivity onto the target
decls:
  - GlobalTheory.BigOn.OntoPath.onto_path_alt
  - GlobalTheory.T.onto_x_of_all_estimates
  - GlobalTheory.BigOn.ontoX_of_twist_shares_exp_alt
  - GlobalTheory.BigOn.ontoX_of_hypotheses_alt_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Surjectivity onto the target

This section proves the surjectivity statement of Section 1: at almost all points of a family, and for all large constants, the map of the point is onto its target. The proof joins nine statements at the record objects of the points: the runs and the rationality, the geometric and page statements of Section 2, the rank at the twisted places, and four bounds, for the twist, the share, the bad places and the exponents. Each of the nine is a statement of Sections 2 to 9 or follows from them. The published inputs are the eleven of Sections 4, 7 and 8 and one more, the classification of the cuspidal characters of $\mathrm{GL}_d(\mathbb{F}_q)$. The result is one half of [the main theorem of Section 1](/proof/unitary-hypotheses/). The background on [the finite groups $\mathrm{GL}_d(\mathbb{F}_q)$](/learn/groups/#finite-groups-of-lie-type) is in Volume 1.

Keep the notation of Sections 2 and 3. Let $p$ be a point with a pair of runs $r$, and $O$ a recorded object at $p$. The object has lattices $Z_g(j)$, $\Theta_0(v, j)$, $\Theta_J(v, j)$ and $e_J(v, j)$ at the twisted places $v$ and the levels $j$, numbers $\varepsilon_0(v, j)$, a group $U$, a share $y$, sizes $n_Z(j)$ and $d_0(j)$, and the point has a dimension $D$. Write $\bar v$ for the conjugate place and $\ell_v$ for the residue characteristic.

**Definition 5.10.1 (Rationality and maximality).** The *rationality statement* is the closed property: eventually at the points of $\mathcal{F}$, each rich point is twisted rational with trivial weights. The *maximality statement* is the closed property: eventually at the points, for each rich point $p$, each twisted place $v$ and each level $j$, the trace lattice at $(v, j)$ is spanned over the classes of $U$ with the character $\psi_0^{-1}$, away from the own prime.

Lean: `GlobalTheory.BigOn.RationalityStatement'` (also `GlobalTheory.BigOn.MaximalityStatement`).

**Definition 5.10.2 (Rank at places).** The object $O$ has the *rank at places* if, for each twisted place $v$ and each level $j$, the image of $\Theta_0(v, j)$ and the lattice $e_J(v, j)$ are lattices in $Z_g(j)$, and

$$\Theta_0(v, j)_v \subseteq \Theta_J(v, j)_v$$

after localization at $v$.

Lean: `GlobalTheory.TraceClassRank.RankAtPlaces`.

**Definition 5.10.3 (Twist, share and bad share).** The object $O$ has:

1. the *twist bound* if there are numbers $\varepsilon_0(v, j) \ge 0$ such that, for each twisted place $v$ and level $j$, the index of the third twisted lattice in the cut of $Z_g(j)$ is at most the index of $e_J(v, j)$ plus the ramification of $v$ times $\varepsilon_0(v, j)$, and for each twisted place $w$

$$\sum_j \big( \varepsilon_0(w, j) + \varepsilon_0(\bar w, j) \big) \le \frac{2}{\ell_w^{2}};$$

2. the *share bound* if for each $j$ there is $\epsilon \le y$ with $(1 - \epsilon)\, n_Z(j) \le |U|\, d_0(j)$;
3. the *bad share bound* if for each $j$ there is $\delta$ with $0 \le \delta \le 1/4$ and $(1 - \delta)\, d_0(j) \le D$.

The *twist*, *share* and *bad places statements* are the statements for all record objects of Section 2 with these properties.

Lean: `GlobalTheory.BigOn.TwistStatement'` (also `GlobalTheory.BigOn.ShareStatement` and `GlobalTheory.BigOn.BadPlacesStatement`).

**Theorem 5.10.4 (Surjectivity from nine statements).** Assume the two runs statement, the rationality statement, the geometric statement, the rank at places for all record objects, the twist, share, bad places and exponent statements, and the page statement. Then the surjectivity statement holds.

Lean: `GlobalTheory.BigOn.OntoPath.onto_path_alt` (also `GlobalTheory.T.onto_x_of_all_estimates`, a second name).

*Proof.* Join the nine closed statements. Seven of them are statements for all record objects, each with a threshold $c_i$ for the bad constant records. Put

$$c_0 = \max(c_1, \dots, c_7, 1),$$

and take the constant record $c = (c_0, 14, 66 c_0 + 4)$. It is bad: its second entry is $14$ and its third is $66 c_0 + 4$. Each of the seven statements applies to $c$ and gives a height threshold $x_i$; the runs and rationality statements give two more. Let $C_E$ be the error constant of $c$, and put $C_0 = 2 \max(C_E, 0)$.

Let $p$ be a rich point beyond all the height thresholds, and $C \ge C_0$. The two runs statement gives a good pair of runs $r$, pinned at the own primes, and $p$ is twisted rational. The canonical and half conditions of $p$ give a recorded object $O$ at $p$ for $r$ and $c$. So the seven statements hold for $O$: the geometric bounds on the sup, the span, the lemma set, the data, the index and the depth; the rank at places; the twist, share and bad share bounds; the exponent bound at each $(C, C_H)$; and the page, size, $x$, bad, level, $y$ and tie conditions of the page statement.

The places of single index of $p$ are twisted, so $p$ has links: the core data, a uniformity, base links and the rational run conditions. From the record, the links and the rationality we get the leaf identity and the second twist inclusion of $O$. The depth bounds at $(C_E, C_H)$ give four depth conditions. Now the chain bound for the twisted places along the two runs takes all of these and gives an error term $\mathrm{err}$ with the split part bound at $(C_E, C_H)$. From it, the clauses of the surjectivity relation hold at the number record of $p$ at $(C_E, C_H)$ with the error $\mathrm{err}$, and the dimension of the map of $p$ is the size $D > 0$ of the rational runs. The exponent bound gives $J_0 \ge 0$ at each twisted place. Since $C \ge 2 \max(C_E, 0)$, the canonical passage from the clauses with error to the relation itself gives that the map of $p$ is onto the target at $(C, C_H)$. $\square$

**Theorem 5.10.5 (Surjectivity from four bounds).** Assume the export statement and the twist, share, bad places and exponent statements. Then the surjectivity statement holds.

Lean: `GlobalTheory.BigOn.ontoX_of_twist_shares_exp_alt`.

*Proof.* Apply the theorem above. The four bounds are given. The other five statements hold with no input: the page statement holds by Section 2 and gives the geometric statement; the two runs statement holds by [Section 5.3.4](/entry/big-on-runs-st/); the rationality statement holds at each rich point; and the rank at places follows from the maximality statement, which holds with no input, the geometric statement and [the comparison off the own prime](/entry/compare-off-own-at-runs-alt/). The export statement is not used. $\square$

The remaining published input is the classification of the cuspidal characters of the finite general linear group. Let $g$ be a prime, $d \ge 1$, and let a *label datum* at $g$ fix a choice of Teichmüller characters for the finite fields $\mathbb{F}_{g^n}$.

**Theorem 5.10.6 (Cuspidal characters of $\mathrm{GL}_d(\mathbb{F}_g)$).** For each prime $g$, each label datum $L$ at $g$ and each $d \ge 1$ there is a map $\tau$ from the polynomials over $\mathbb{F}_g$ to the class functions on $\mathrm{GL}_d(\mathbb{F}_g)$ such that:

1. for each prime label $P$ of degree $d$, $\tau(P)$ is a cuspidal character with label $P$ for $L$, of degree
$$\tau(P)(1) = \prod_{i = 1}^{d - 1} (g^{i} - 1);$$
2. $\tau$ is injective on the prime labels of degree $d$;
3. each cuspidal irreducible character of $\mathrm{GL}_d(\mathbb{F}_g)$ is $\tau(P)$ for a prime label $P$.

Lean: `GlobalTheory.Published.GreenCuspidal` (also `GlobalTheory.GLq.Green`, the statement it unfolds to).

This is part of the determination of the characters of $\mathrm{GL}_d(\mathbb{F}_q)$ by Green (*The characters of the finite general linear groups*, 1955).

**Theorem 5.10.7 (The surjectivity statement).** Assume the classification of cuspidal characters of $\mathrm{GL}_d(\mathbb{F}_g)$, that regular algebraic cusp forms are cohomological, the theorem on $\ell$-adic characters of Hecke characters, Chebotarev in degree one, the theorem on Galois representations of polarized cusp forms, base change for definite unitary groups, the theorem on crystalline lattices, the second theorem on $\ell$-adic characters at the places above $\ell$, rapid decay of cusp forms, the local Langlands correspondence, the classification of the discrete series and the Casselman-Wallach theorem. Then the surjectivity statement holds.

Lean: `GlobalTheory.BigOn.ontoX_of_hypotheses_alt_alt`.

*Proof.* We get the five statements of the last theorem.

1. *Export.* The theorem on $\ell$-adic characters contains a global Artin map. This gives global Artin reciprocity, then the existence of ray class fields, and the rational series statement. With rapid decay, the discrete series and the Casselman-Wallach theorem, Section 4 gives the export statement.
2. *Twist.* The page statement holds with no input, and Section 2 gives the geometric statement. With the maximality statement and the comparison off the own prime it gives the rank at places. The export, geometric and rank statements give the twist statement.
3. *Share.* The run model statement of Section 3 gives a share statement for the run models, and from it the share statement.
4. *Bad places.* The classification of cuspidal characters and the run model statement give a bad share statement for the run models, and from it the bad places statement.
5. *Exponent.* The eight inputs of Section 9 give the exponent statement.

Now apply the surjectivity from four bounds. $\square$

The classification of cuspidal characters enters in step 4: the bad places of a run model are the places where the level group has a cuspidal type, and the degree formula of Green bounds the share $d_0(j)$ of these types against the dimension $D$. This is our reading of the names in the bad share lemma.

**Remark 5.10.8 (Formalization).** The theorem from nine statements is in [OntoPath.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OntoPath.lean#L18), and its second name in [OntoPathStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OntoPathStatement.lean#L13), a one-line call with `maxHeartbeats` set to 1000000. The proof introduces the hypothesis that the family satisfies the condition of Section 1 and does not use it (line 23). The constant record is fixed at line 26 as $(c_0, 14, 66 c_0 + 4)$, so only the least bad constant record is used. The condition of the page statement that the size $b$ of the object is that of the point is dropped (the pattern `-` at line 61), and so is the last of the links (line 64). The theorem from four bounds is in [OntoXOfTwistSharesExp.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OntoXOfTwistSharesExp.lean#L21); its first argument is bound by `intro _` at line 22 and never used. It proves the page, geometric and rank statements again, with second names of the lemmas that the main theorem also calls, so these are proved twice. A parallel copy with the older wrapper is in [the divisor proofs](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/OntoXOfTwistSharesExp.lean#L21). The main theorem is in [OntoXOfPrints.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OntoXOfPrints.lean#L28); it finds the arguments of the export theorem by `with_reducible assumption`. All twelve inputs are used. The words "prints" and "hypotheses alt alt" do not describe the statement. The definitions of the statements are in [ExportSt.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportSt.lean#L31), the leaf conditions in [ExampleSatisfiesConditionsAtFive.lean](lean:Formalism/LocalToGlobal/IndefiniteForms/IndefiniteTree/ExampleSatisfiesConditionsAtFive.lean#L288), and Green's statement in [LabelDatum.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/LabelDatum.lean#L108). We have not unfolded the chain bound for the twisted places, the surjectivity relation, the label datum, the cuspidal labels or the bad share lemma; the description of the role of Green's theorem is our reading of names.
