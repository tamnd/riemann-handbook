---
title: Regular charts at finite places and the laws of abelian schemes
decls:
  - GlobalTheory.Reg.sCharts_and_transfer_of_good_level
  - GlobalTheory.T.transfer_bounds_algebraic_to_all_points_of_models
  - GlobalTheory.Reg.transfer_of_models
  - GlobalTheory.AbLaw.AllLaws.laws_of_h0_eq_one
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Regular charts at finite places and the laws of abelian schemes

The last two results of the chapter are about the moduli space itself and not about its metrics. The first says that at every finite place the moduli space has a finite family of normal charts over a complete discrete valuation ring, and that bounds on sections at algebraic points transfer to all points. The second derives the full list of laws of abelian schemes that the volume uses from one fact: a principal polarization on an abelian variety over an algebraically closed field has a one dimensional space of sections.

### Sections, valuations and points

Let $E$ be a CM field with host $H$, let $D$ be a datum with $p + q \geq 1$, let $l$ be a level that is good at every prime, and let $X_o$ be the moduli scheme, with coefficient field $F$. A rule is a rational section of a power of the Hodge bundle on $X_o$, and $\operatorname{sec}(a, n)$ is the space of rules of weight $a$ and level $n$.

Let $\lambda$ be a finite place of $F$. A frame point over a complete discrete valuation ring $T$ is a point of $X_o$ over the fraction field of $T$ with a frame of the Hodge bundle. It is integral if it extends over $T$. Each integral frame point $y$ over a ring that lies over $\lambda$ gives a valuation $f \mapsto v_y(f)$ on rules, the normalized valuation of $f$ evaluated at $y$. The set $\operatorname{val}_\lambda$ is the set of these valuations for algebraic points $y$, that is, points whose coordinates are algebraic over $F$. For an integral frame point $Q$ of trivial class, write $\operatorname{ord}_Q(f)$ for the order of $f$ at $Q$.

A chart system at $\lambda$ is a complete discrete valuation ring $O$ of characteristic $0$ over $\lambda$, and a finite family of normal flat domains $A_j$ of finite type over $O$, with maps from rules to the fraction fields of the $A_j$. It covers the points of trivial class if every such point factors through one of the $A_j$. It fits a family $w_1, \dots, w_m$ of rules if on each chart one $w_k$ is not zero and all the others are multiples of it with coefficients in $A_j$.

Let $C(a, n) \subseteq \operatorname{sec}(a, n)$ be a family of subspaces.

**Definition 10.21.1.** The first regularity law holds for $C$ if every $f \in C(a, n)$ with $v(f) \geq 0$ for all $v \in \operatorname{val}_\lambda$, for some $\lambda$, has $\operatorname{ord}_Q(f) \geq 0$ at every point $Q$ of trivial class. The second regularity law holds for $C$ if the following holds for all $w_1, \dots, w_k \in C(a_L, n_L)$, $e \in C(a_E, n_E)$ and $c' \geq 0$. Assume there are $\lambda$ and $\nu$ such that for every $v \in \operatorname{val}_\lambda$ we have $v(e) \geq 0$, some $v(w_i)$ is finite, and
$$
\min_i v(w_i) \leq \nu + c' v(e)
$$
when $v(e)$ is finite. Then at every point $Q$ of trivial class, $\operatorname{ord}_Q(e) \geq 0$, and $\min_i \operatorname{ord}_Q(w_i) \leq c' \operatorname{ord}_Q(e)$ when $\operatorname{ord}_Q(e)$ is finite.

So a bound that holds at algebraic points, up to a constant $\nu$, holds at all points of trivial class with no constant.

### Transfer of bounds

**Theorem 10.21.2 (Transfer from models).** Assume the twist law for sections. Let the evaluation laws hold for the frames of $X_o$, let the transition units of integral frames be units, and assume a model of $X_o$ exists over the valuation ring of every finite place, with an invertible pushforward of the Hodge line. Then the cusp forms of every uniformization satisfy the regularity law, and every family $C$ with $C(a, n) \subseteq \operatorname{sec}(a, n)$ satisfies the first and the second regularity laws.

Lean: `GlobalTheory.Reg.transfer_of_models` (also `GlobalTheory.T.transfer_bounds_algebraic_to_all_points_of_models`, a second name).

*Proof.* Step 1: normal charts. At every finite place $\lambda$, the model over the valuation ring of $\lambda$, the twist law and the evaluation laws give a system of normal charts at $\lambda$ that covers the points of trivial class.

Step 2: the regularity law. The transfer law for normal charts gives the regularity law for the cusp forms. On each chart a rule is a fraction in a normal domain, and a fraction that is integral at the algebraic points is integral at all height one primes, hence integral.

Step 3: the first law. Integrality at the trivial valuations of normal affine charts gives the first law.

Step 4: the second law. Let $w_1, \dots, w_k$ and $e$ satisfy the hypothesis. Since some $v(w_i)$ is finite for every $v \in \operatorname{val}_\lambda$, the $w_i$ have no common zero. The combined bound at trivial valuations of charts then gives the second law: on a chart where one $w_k$ divides the others, the bound at algebraic points passes to the orders at the points of trivial class. $\square$

**Theorem 10.21.3 (Charts and transfer at a good level).** Assume the uniformization statement for the first part of the toroidal theory and that the moduli scheme exists at every level. Let $p + q \geq 1$ and let $l$ be good at every prime. Then:

1. at every finite place $\lambda$ there is a chart system that covers the points of trivial class;
2. for every family $w_1, \dots, w_m$ in one $\operatorname{sec}(a, n)$ with no common zero there is such a chart system that fits the family;
3. the conclusions of the transfer theorem hold.

Lean: `GlobalTheory.Reg.sCharts_and_transfer_of_good_level`.

*Proof.* The twist law for sections is one of the laws of abelian schemes, which are proved below. The evaluation laws and the units of transitions hold for the frames of $X_o$. At a good level, the first part of the toroidal theory gives a model of $X_o$ over the valuation ring of every finite place, with an invertible pushforward of the Hodge line. Normal charts at every finite place give parts 1 and 2. The transfer theorem gives part 3. $\square$

### The laws of abelian schemes

The laws of abelian schemes are a list of facts that the volume uses about abelian schemes over a base $S$ with a polarization $L$. They include: the sections of $L^n$ have rank $n^g$ over algebraically closed fields; sections commute with base change; some power of $L$ is ample; the theta bundle of $L^n$ at a point $x$ is locally trivial exactly when $x$ is $n$ torsion; the theorem of the cube and the theorem of the square; the Weil pairing is alternating and nondegenerate; symmetric lifts of odd order exist and are unique; the Heisenberg group acts irreducibly on sections; rigidity; Serre's lemma that an automorphism fixing enough torsion is the identity; extension of line bundles over regular bases; and quotients by finite flat subgroups. The further laws add base change of sections for any base, the twist law, character pairs and density of the smooth locus.

**Theorem 10.21.4 (Laws from one section).** Assume that for every algebraically closed field $K$ and every principally polarized abelian variety over $K$, the space of sections of the polarization has dimension $1$. Then all laws of abelian schemes and the further laws hold.

Lean: `GlobalTheory.AbLaw.AllLaws.laws_of_h0_eq_one`.

*Proof.* Step 1: laws without cohomology. Smooth geometrically connected schemes over a field are geometrically integral. Rigidity, the projective base change, the base lemma and the extension of characters hold without any cohomology.

Step 2: the cube. The theorem of the cube for a generator, with the finiteness and growth of sections, gives the square, pullbacks under multiplication, powers of kernels, the Weil pairing, symmetric lifts, nondegeneracy, character pairs and the multiplication by $q$ map.

Step 3: the rank of sections. The hypothesis in rank $1$, together with the cube, the multiplication by $q$ map and the growth of sections, gives rank $n^g$ for the sections of $L^n$ over algebraically closed fields. Multiplication by $n$ follows by decomposition.

Step 4: vanishing and base change. A very ample power, Serre vanishing and the vanishing of the first cohomology of nontrivial translates give the vanishing of higher cohomology of powers. A perfect complex of sections then gives base change of sections for all bases and the twist law.

Step 5: Heisenberg. The Heisenberg group acts linearly, and the Weil pairing makes the action irreducible, since the space of sections has the right rank.

Step 6: ampleness and good points. Sections have no base points and separate points, so a power of $L$ is ample. Irreducibility gives good points.

Step 7: Serre's lemma. An automorphism that fixes the torsion of order $n \geq 3$ has finite order, and an endomorphism that is divisible by all powers is $0$. With rigidity this gives Serre's lemma over any base.

Step 8: extension and quotients. Smooth schemes are regular, regular local rings are factorial, and line bundles extend from open sets. Finite flat subgroups have quotient schemes, and these quotients are abelian schemes. $\square$

The hypothesis is itself proved: the rank of sections of a principal polarization is $1$. So all the laws hold with no hypotheses.

**Remark 10.21.5 (Formalization).** The charts theorem is at `Development/AbelianVarietyTheory/Proofs/GenericRegularity/SChartsAndTransferOfGoodLevel.lean:24`. It takes the twist law from the unconditional laws `GlobalTheory.abelianSchemeLaws_all` (line 27) and discards the third part of the evaluation laws with `-` (line 28). It builds the normal charts at every place for part 1 (line 34), and then the transfer theorem builds the same charts again (`TransferBoundsAlgebraicToAllPointsOfModels.lean:24`). The model at a place is obtained by updating a choice of moduli schemes at the level $l$ (lines 29 to 33). The transfer theorem is at line 22 of its file; its second name is at `TransferBoundsAlgebraicToAllPointsOfModelsStatement.lean:15`, under `maxHeartbeats 1000000`, and is proved by `first | exact @GlobalTheory.Reg.transfer_of_models | ...`. The regularity laws are defined twice, in `Formalism/LocalToGlobal/ProjectiveLattices/RegularityR2Quotient.lean:23` and in `RegQFree.lean:25` of the same folder, with the same body, and the points `QPt` are defined in both files. The laws theorem is at `Development/AbelianVarietyTheory/Proofs/AbelianSchemeLawProofs/LawsOfH0EqOneClosedFields.lean:64`, and its hypothesis is discharged in `AbelianSchemeLawsUnconditional.lean:15`. The cube generator gives the square, the pullback law, the kernel powers and the symmetric lifts at line 71, and lines 72 to 77 derive the same facts again as `sq`, `mp`, `ker` and `sym`; the final tuple (line 117) uses the first copies for the laws and the second copies only as inputs to later steps.
