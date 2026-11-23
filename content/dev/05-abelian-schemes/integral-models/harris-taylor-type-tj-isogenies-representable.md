---
id: harris-taylor-type-tj-isogenies-representable
title: Isogenies of type T_j are represented by a finite étale scheme
kind: theorem
decl: GlobalTheory.T.harrisTaylor_typeTj_isogenies_representable
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HarrisTaylorTypeTjIsogeniesRepresentableStatement
covers: 479
status: drafted
drafted_by: writer@claude
---
This theorem says that the $c$-isogenies of type $T_j$ out of a Harris-Taylor object are classified by a finite étale scheme. It is a second name for [the lemma that builds this scheme](/entry/isog-rep-exists-rep/), which has the proof. It sits below the [six facts about the Kuga-Sato tower](/entry/kodaira-spencer-of-weight-one/).

## Statement

Let $p$, the datum $D$ with CM field $F$ and element $\omega$, the base $b$ over $R$, and the objects $o = (A, \iota, P, \eta)$ of level $N$ be as in [the integral model](/entry/model-nonempty/). Let $u_r = (p, \omega - r) \subseteq \mathcal{O}_F$ for $r \in \mathbb{Z}$.

For objects $o, o'$ over $S$ and $c \in \mathbb{N}$, a homomorphism $\psi \colon A \to A'$ is a *$c$-isogeny* (`IsPIsog`) if $c$ is a power of $p$, $\psi$ commutes with the action of $O$, $\eta' = \psi \circ \eta$, $\psi$ pulls the bundle $P'$ back to $P^{\otimes c}$, and there is $\psi'$ with $\psi'\psi = c$ and $\psi\psi' = c$. It has *type $T_j$* at $w$ (`IsTj`) if for each geometric point $x$ of $S$ of characteristic $0$: each point of $(\ker \psi)_x$ killed by a power of $u_r$ is killed by $w$, and $(\ker\psi)_x$ has $N(w)^{mj}$ points killed by $w$.

**Theorem.** Let $R$ be noetherian, $p$ a unit in $R$, $N \geq 3$ prime to $p$, $w$ a maximal ideal of $\mathcal{O}_F$ with $u_r \subseteq w$, $j \leq n$, $c = p^e$ with $e > 0$ if $j > 0$, and $m = 1$. Let $S$ be a locally noetherian scheme over $R$ and $o$ an object over $S$. Then there are a finite étale $Y \to S$, the pullback $o_0$ of $o$ to $Y$, an object $o'$ over $Y$ and a $c$-isogeny $\psi \colon A_0 \to A'$ of type $T_j$ with this property: for each $x \colon T \to S$, each pullback $o_1$ of $o$ along $x$ and each $c$-isogeny $\psi_1 \colon A_1 \to A_1'$ of type $T_j$, there is a unique $y \colon T \to Y$ over $S$ for which maps $o_1 \to o_0$ and $o_1' \to o'$ over $y$ exist that carry $\psi$ to $\psi_1$.

## Proof

The proof is `exact ES.IsogRep.exists_rep`, see [the lemma that builds Y](/entry/isog-rep-exists-rep/).

## In the Lean code

The theorem is in [HarrisTaylorTypeTjIsogeniesRepresentableStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorTypeTjIsogeniesRepresentableStatement.lean#L9). `IsPIsog`, `IsTj` and `uIdeal` are in [ExistsTjCorrDiagModel.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsTjCorrDiagModel.lean#L55). Its users include `ES.exists_tjCorr_finiteEtale`, which we have not opened. We have not checked type $T_j$ against Harris and Taylor (Annals of Math. Studies 151, 2001). `IsTj` tests only geometric points of characteristic $0$. So over a base with no such points, for example a scheme over $\mathbb{F}_\ell$, every $c$-isogeny has type $T_j$.
