---
id: ds-exhaust
title: Every square-integrable representation of U(p,q) is a discrete series
kind: theorem
decl: CompanionTheory.RgExh.dsExhaust
module: CompanionTheory.RealGroups.DiscreteSeries.DiscreteSeriesClassification.DiscreteSeriesExhaustion.DsExhaust
covers: 1676
status: drafted
drafted_by: writer@claude
---
This theorem says that each irreducible square-integrable [[unitary representation|74BPYJNZTM]] of $\mathrm{U}(p,q)$ is a discrete series. The same file turns it into `discreteSeriesClassification` and `discreteSeriesCover`, which the [literature theorem](/step/every-character-of-literature/) uses. Below this theorem are 1,676 declarations of the proof.

## Statement

Let $\varepsilon \in \{\pm\}^n$ be a signature, $J = \operatorname{diag}(\varepsilon)$, $G = \{g : g^* J g = J\} \cong \mathrm{U}(p,q)$ and $K = G \cap \mathrm{U}(n)$. Let $\rho_c(a) = \tfrac12(\#\{b > a\} - \#\{b < a\})$ over $b$ of the sign of $a$, and $\rho_n$ the same over $b$ of the other sign. A *Harish-Chandra parameter* is a strictly decreasing $\mu \in \mathbb{R}^n$ with $\mu_a - \tfrac{n-1}{2} \in \mathbb{Z}$.

A representation $\sigma$ of $G$ on a Hilbert space $H \neq 0$ is *square-integrable irreducible* if it is unitary, strongly continuous and irreducible, with matrix coefficients in $L^2(G)$ for the measure `muG`. It is a *discrete series with parameter* $\mu$ (`IsDS`) if also the $K$-type with highest weight $\Lambda = \mu + \rho_n - \rho_c$ occurs, and each $K$-type $\Lambda'$ that occurs has $\|\Lambda + 2\rho_c\|^2 \leq \|\Lambda' + 2\rho_c\|^2$.

**Theorem.** Let $\sigma$ be square-integrable irreducible. Then there are a Harish-Chandra parameter $\mu$ and a permutation $s$ that keeps the order inside each sign class such that $\sigma$, renumbered by $s$, is a discrete series with parameter $\mu$ for the signature $\varepsilon \circ s$.

This has the shape of the exhaustion half of Harish-Chandra's classification of the discrete series (Acta Math. 116, 1966), with each discrete series given by its lowest $K$-type.

## Proof

The proof works with the [[Harish-Chandra module|2MKHH636C3]] $X$ of $K$-finite vectors. A *step* in direction $s$ tensors $X$ with $\mathbb{C}^n$ and keeps one generalized eigenspace of the operator $u \mapsto \bigl(\sum_a E_{ab} u_a\bigr)_b$. The character $\chi \in \mathbb{C}^n$ of $X$ comes from the quantum determinant. `dsExhaust` applies `exhaustion_finite_length` to four facts:

1. `infinitesimal_character_shift`: a step in direction $s$ moves the character from $\chi$ to $\chi + e_s$.
2. `hecke_algebra_exhaustion`: along a path of steps with $\chi_r \neq \chi_s + 1$, if the end has a scalar character, then the end is simple and determines the start up to isomorphism.
3. `decay_estimate`: if such a path ends at labels far enough out, the end module embeds into smooth $L^2$ functions on $G$.
4. `far_regular_exhaustion`: a unitary module with integral weights whose character has entries far apart is an algebraic discrete series (`AlgDS`).

The combination `RgExhFin.finish` goes as follows. Take the module $D$ of $\sigma$ (`kModOf`), simple with scalar character $\chi$ (`startMod`). Choose a path to far labels (`pathExists`). By facts 3 and 4 the end of $D$ is an algebraic discrete series with data $d_0$. `arrCount` gives sets $A$ and $A'$ of equal finite size: discrete series data with character $\chi$ and with the end character. Path ends give a map $A \to A'$ (`dsOfArr`), injective by fact 2 and `dataUniq`, so onto. So $d_0$ is the end of some $d \in A$, fact 2 makes $D$ the module of $d$, and `dsOfData` gives `IsDS`.

## In the Lean code

Files: the theorem [DsExhaust.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/DsExhaust.lean#L14), the statement [DiscreteSpectrumKFiniteDecomposition.lean](lean:Development/AbelianVarietyTheory/Statements/CuspFrameWeights/DiscreteSpectrumKFiniteDecomposition.lean#L31), the combination [HasCharOfScalChar.lean](lean:CompanionTheory/SpectralGeometry/LocalGlobalProofs/StableLattices/HasCharOfScalChar.lean#L52).

- `exhaustion_finite_length` has type `Finish`, the implication from the four facts to `DSExhaust` ([Development.lean](lean:CompanionTheory/RealGroups/DiscreteSeries/DiscreteSeriesClassification/DiscreteSeriesExhaustion/Development.lean#L6)). All four are proved, so `dsExhaust` has no hypothesis.
- `decay_estimate` takes `StepChar` as an argument, so `infinitesimal_character_shift` is passed twice. It only renames the theorem `GlobalTheory.T.InfinitesimalCharacterStatement`.
- `IsDS` has a second copy with the same body in [DiscreteSeriesUnitary.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/FockTheta/DiscreteSeriesUnitary.lean#L69).
- The two literature theorems ignore their argument `O` ([EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L353)).
- We have not unfolded `muG`, `IsCRepOn` or the target `smD ε (rreg ε)` of the $L^2$ embedding.
