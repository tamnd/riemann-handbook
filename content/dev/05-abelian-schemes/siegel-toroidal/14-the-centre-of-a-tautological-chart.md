---
title: The centre of a tautological chart
decls:
  - GlobalTheory.T.tautologicalChart_centre_isCompletedEtaleLocalMap
  - GlobalTheory.TChartEt.isEtaleCompletion_tautChart
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The centre of a tautological chart

A [pre-chart](/entry/exists-chart-at/) at a point $x$ of the normalized blowup $S$ asks, in its first clause, that the map $\mathcal{O}_{S,x} \to R$ be an étale completion and that $\mathcal{O}_{S,x} \to R \to k_R$ be formally unramified. This section proves this clause for the ring $R$ of a tautological chart that is a family for $F$ and whose centre is $x$. The argument has two halves. The separation theorem of the section on [the centre of a chart](/entry/sep-st/) shows that $R$ is quasi-finite over $\mathcal{O}_{S,x}$. A Galois argument shows that no nontrivial automorphism of a finite extension of $R$ can fix $\mathcal{O}_{S,x}$ while acting trivially on the residue field. Quasi-finiteness and this rigidity together force the map to be an étale completion. The result is used in the proof that [charts exist on the normalized blowup](/entry/chart-st5-holds/).

**Definition 9.14.1 (Étale completion).** Let $f : A \to R$ be a map of local rings. Then $f$ is an *étale completion* if $f$ is flat, $\mathfrak{m}_A R = \mathfrak{m}_R$, and the residue field $k_R$ is a finite $A$-module through $A \to R \to k_R$.

Lean: `GlobalTheory.Toroidal.IsEtaleCompletion`.

For example, if $A$ is a noetherian local ring and $R = \hat{A}$ is its $\mathfrak{m}_A$-adic completion, then $A \to \hat{A}$ is an étale completion: completion is flat, $\mathfrak{m}_A \hat{A}$ is the maximal ideal of $\hat{A}$, and the residue fields agree ([completion](/learn/commutative-algebra/#completion)). In a chart, $R$ plays the part of the completion of $S$ at $x$, up to a finite extension of the residue field. The name comes from [flat and étale algebras](/learn/commutative-algebra/#flat-and-tale-algebras): flatness and $\mathfrak{m}_A R = \mathfrak{m}_R$ are the conditions of an unramified flat map at the closed point, and the second conclusion of the theorem below adds that the residue extension is formally unramified.

**Definition 9.14.2 (Galois rigid).** Let $f : A \to R$ be a ring map. Then $f$ is *Galois rigid* if the following holds for each local CN domain $R'$, each injective finite ring map $\theta : R \to R'$ and each automorphism $\sigma$ of $R'$ of finite order: if $\sigma$ fixes $\theta(f(a))$ for each $a \in A$ and $\sigma(\theta(r)) - \theta(r) \in \mathfrak{m}_{R'}$ for each $r \in R$, then $\sigma$ fixes $\theta(r)$ for each $r \in R$.

Lean: `GlobalTheory.TChart.GalRigid`.

If $f$ is surjective, then $f$ is Galois rigid, since each $\theta(r)$ is some $\theta(f(a))$. The condition says that an automorphism of a finite extension of $R$ that fixes $A$ and acts trivially modulo the maximal ideal fixes $R$.

We use a criterion for étale completions. Let $O$ be a local normal domain of characteristic $0$ that is essentially of finite type over $\mathbb{Z}$, and let $f : O \to R$ be a local map to a noetherian local domain that is $\mathfrak{m}_R$-adically complete. Assume that every prime of $R$ that contains $\mathfrak{m}_O R$ is $\mathfrak{m}_R$, that $k_R$ is finite over $O$, that $\dim O \le \dim R$, and that $f$ is Galois rigid. Then $f$ is an étale completion and $O \to R \to k_R$ is formally unramified. We use only the statement of this criterion. The first two conditions say that $R$ is quasi-finite over $O$ at its closed point.

Fix $g \ge 1$, an odd $n \ge 3$, a Siegel family $F$ of genus $g$ and level $n$ over $\Lambda_n$, and a polarization function $\varphi$ of rank $g$ with no self-intersections.

**Theorem 9.14.3 (The centre of a tautological chart).** Assume the theorem on [separation at the centre](/entry/sep-st/). Let $(Z, z, i, \mathcal{O}_Z(1))$ be minimal compactification data for $F$, and let $(\pi, j, B)$ be blowup data of order $d$ for $\varphi$, with $\pi : S \to Z$ and $j : X \to S$ an open immersion. Let $C$ be a tautological chart of genus $g$ and level $n$ for $\varphi$, with ring $R$. Let $G_1$ be a commutative group scheme over $R$, $y : \operatorname{Spec} K_R \to X$, $\alpha_1$ a map from the generic fibre of $G_1$ to $A$, and $\xi : \operatorname{Spec} R \to S$, such that $C$ is a family for $F$ with $(G_1, y, \alpha_1)$ and $j \circ y = \xi \circ \iota_R$. Let $x = \xi(\mathfrak{m}_R)$. Then the map $\mathcal{O}_{S,x} \to R$ given by $\xi$ is an étale completion, and $\mathcal{O}_{S,x} \to R \to k_R$ is formally unramified.

Lean: `GlobalTheory.TChartEt.isEtaleCompletion_tautChart` (also `GlobalTheory.T.tautologicalChart_centre_isCompletedEtaleLocalMap`, a wrapper).

*Proof.* We check the hypotheses of the criterion with $O = \mathcal{O}_{S,x}$.

$O$ is a local normal domain, since $\pi$ is a normalized blowup and so $S$ is normal. $O$ has characteristic $0$: the structure map of $F$ is smooth, hence flat, over $\Lambda_n$, so the local rings of $X$ have characteristic $0$. Let $w$ be the generic point of $\operatorname{Spec} R$. Since $j \circ y = \xi \circ \iota_R$, we have $\xi(w) = j(y(w))$, and $\xi(w)$ specializes to $x$. So there are ring maps $O \to \mathcal{O}_{S, \xi(w)} \to \mathcal{O}_{X, y(w)}$, and a ring with a map to a ring of characteristic $0$ has characteristic $0$. $O$ is essentially of finite type over $\mathbb{Z}$: the map $z \circ \pi$ is projective, hence of finite type, and $\Lambda_n$ is of finite type over $\mathbb{Z}$. $R$ is a noetherian complete local domain, as $C$ completes at a prime.

A theorem on quasi-finiteness of tautological charts, which takes the separation theorem as input, shows that every prime of $R$ that contains $\mathfrak{m}_O R$ is $\mathfrak{m}_R$ and that $k_R$ is finite over $O$. A theorem on dimensions, which uses this finiteness, gives $\dim O \le \dim R$. A theorem on Galois rigidity of tautological charts, which uses $n \ge 3$, shows that $O \to R$ is Galois rigid. We use only the statements of these three theorems. The criterion now gives both conclusions. $\square$

The separation theorem enters only through quasi-finiteness.

**Remark 9.14.4 (Formalization).** The theorem takes the separation theorem as a hypothesis `SepSt`; the caller in the proof of the chart theorem passes `T.chartSeparation_data_defined_over_centre_field`. The facts on the stalk are four helper lemmas: injectivity of flat local maps, characteristic $0$ of stalks of a flat scheme over a domain of characteristic $0$, essential finite type of stalks over $\mathbb{Z}$, and characteristic $0$ at the centre ([TautologicalChartCentreIsCompletedEtaleLocalMap.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TautologicalChartCentreIsCompletedEtaleLocalMap.lean#L23)). The definition of an étale completion asks for flatness, $\mathfrak{m}_A R = \mathfrak{m}_R$ and finiteness of the residue field; it does not ask that $R$ be complete, and it does not ask for separability, which comes from the second conclusion ([IsProperToroidalModelStructureMap.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/IsProperToroidalModelStructureMap.lean#L347)). The lemmas on quasi-finiteness, dimension and Galois rigidity, and the criterion, have no entries in this part.
