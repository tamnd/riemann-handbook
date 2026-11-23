---
id: crystalline-universal-part-case-a
title: The universal part of an arc in the unramified case
kind: theorem
decl: GlobalTheory.T.crystallineUniversalPart_caseA
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.CrystallineUniversalPartCaseAStatement
covers: 380
status: drafted
drafted_by: writer@claude
---
This theorem gives condition 11, the universal part `adm14`, of the [thirteen admitted conditions](/entry/admissible-ranks-of-cmdatum/). It is a second name for [`universalPart_caseA`](/entry/universal-part-case-a/), itself a second name for [`universal_general_statement_holds`](/entry/universal-general-statement-holds/), which has the proof.

## Statement

Let $D$, $HW$, $F$, $C_m$ be as in [local lifting theorem B](/entry/theorem-b-closing/). "Case A" means: a prime $\ell \ge 5$, a finite extension $K$ of $\mathbb{Q}_\ell$ inside the maximal unramified extension, and a coefficient field $L$ good for $K$ at level 1. Let $W$ be the Wach module of $HW$ at $(K, L)$, with $n = [K : \mathbb{Q}_\ell]$ letters $i \in \mathbb{Z}/n$.

An *arc datum* $A$ (`ArcP`) has heights $G_0, S, \eta, h$, a type (thin, up or down) for each letter, and a set of *cuts* $c$ with lengths $\mathrm{len}(c)$. A lattice is in the *window* of $A$ if it is crystalline and its jumps at each letter lie in the window of the type.

**Theorem.** Assume:

1. `AdmUnivA`: saturation (`adm5`), the killer at levels, the stability of the uniformizer $\pi_0$ under $\Gamma$, and the arc coordinates (`adm12`);
2. `P9`, a condition on the Wach lattices;
3. `ConclusionH`, one of the lifting statements;
4. $D_{\mathrm{dR}} = D_{\mathrm{cris}}$ for crystalline representations of unramified fields (`DdREqDcrisAll`).

Then in case A, for each arc datum $A$, each integer $m$, each lattice $T_2$ in the window of $A$ with at most $m$ low jumps at each thick letter, and each cut $c$, there are a horizontal family $b_1, \dots, b_d$ in the module of $T_2$ and a set $R$ of at most $m \cdot \mathrm{ro}(c)$ indices with these properties:

- for $k \notin R$, the derivative vectors of $b_k$ lie in the prescribed filtration steps at the "up" letters, and at the "down" letters $\mathrm{Fil}^{-\eta}$ lies in the span of those with $k \in R$;
- each $w$ that meets `InI`, `InFP` and `PoleOK` has coordinates $f_k$, with five integrality conditions for $k \notin R$;
- the invariant families supported on $R$ are generated, modulo $\pi_0$, by at most $m \cdot \mathrm{ro}(c)(\mathrm{len}(c) + 1)$ elements;
- each invariant family comes from an element $u$ of the module.

A second statement, `UnivNNCore`, is an integrality condition of the same kind.

## Proof

The proof is `exact universalPart_caseA`.

## In the Lean code

The theorem is in [CrystallineUniversalPartCaseAStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrystallineUniversalPartCaseAStatement.lean#L8). The conclusion `UniversalComponentCaseA` is `adm14`, that is `UnivL`, with `UnivCore` and `UnivNNCore` in [ArcLiftingSetup.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ArcLiftingSetup.lean#L381). We did not unfold `IsHor`, `InFr`, `InNL`, `InvNL`, `RepVV` or `ro`; the list follows the shape of `UnivCore`.

- The namespace `UnusedSlot80` of `AdmUnivA` and `UniversalComponentCaseA` is misleading: both are used.
- Hypothesis 4 is passed down unchanged through `universal_general_of_restriction` to `universal_general_of_sections`. We did not check whether it is used there.
