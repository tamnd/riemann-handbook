---
id: arithmetic-relations-statement-holds
title: The Chern number relations, the statement form
kind: theorem
decl: GlobalTheory.T.arithmetic_relations_statement_holds
module: Development.AutomorphicSpectrum.Proofs.AlgebraProofs.ArithmeticRelationsStatementHoldsStatement
covers: 2229
status: drafted
drafted_by: writer@claude
---
This theorem is a relay with no content of its own. It states `RelationsStatement` and proves it by calling [the Chern number relations for lattice bundles](/entry/top-rel-relations/). The real content is in that entry. Its only user is [the Hodge lattice flag bound from lattice families](/entry/model-on-hodge-of-family-pos/), which applies it after the descent to the generic fibre.

## Statement

Let $O$ be a discrete valuation ring of characteristic $0$, and let $x$ be coordinates that give a model over $O$ of dimension $d$. Let $D$ be a lattice family on the charts for a prime $p$, an element $w$ and a permutation $\varphi$ of a finite set of labels $\Sigma$, with chart bundles that carry its lattices and local pairs that are flag pairs for them. Then for each $k \geq 1$ and each list $Q$ with $|Q| + k = d + 1$, there is $h \colon \Sigma \to \mathbb{R}$ with

$$c_k(\mathrm{lie}_\tau) + c_k(\mathrm{om}_\tau) = h(\tau) - \frac{\lambda_k(\mathrm{lie}_\tau)}{p - 1}, \qquad p^k h(\tau) = h(\varphi\tau) + \lambda_k(\mathrm{lie}_{\varphi\tau}).$$

[The Chern number relations for lattice bundles](/entry/top-rel-relations/) gives all hypotheses and explains $c_k$ and $\lambda_k$.

## Proof

The proof is `first | exact @GlobalTheory.CompanionTheory.Ar.Num.TopRel.relations | ...`. It applies that theorem.

## In the Lean code

The theorem is in [ArithmeticRelationsStatementHoldsStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/AlgebraProofs/ArithmeticRelationsStatementHoldsStatement.lean#L5). It is used in [ModelOnHodgeFromFamily.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/ModelOnHodgeFromFamily.lean#L119).
