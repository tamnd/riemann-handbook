---
id: pbf-of-disc
title: The projective bundle formula passes from discrete spaces to all spaces
kind: theorem
decl: GlobalTheory.PBFg.pbf_of_disc
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ProjectiveBundleFormulaOfDiscreteSpaces
covers: 394
status: drafted
drafted_by: writer@claude
---
This theorem reduces the projective bundle formula on any space to the formula on discrete spaces. It is the proof behind [projectiveBundleFormula_of_discrete_spaces](/entry/projective-bundle-formula-of-discrete-spaces/), which is step 3 of [the general formula](/entry/projective-bundle-formula-vector-bundle-any-space/). Most of the work is in [pbf_of_model](/entry/pbf-of-model/); this proof supplies its two hypotheses on a fixed cocycle. Below this theorem are 394 declarations.

## Statement

The statement is the one in [projectiveBundleFormula_of_discrete_spaces](/entry/projective-bundle-formula-of-discrete-spaces/): for $q \geq 1$ and a fixed rank $N$, if `PBF q V` holds for each vector bundle $V$ of rank $N$ on each discrete space with `Inv`, then it holds for each vector bundle $V \colon E \to B\mathrm{GL}_N$ on each space $E$ with `Inv q E`.

## Proof

Let $\mathrm{lineSp} = \operatorname{disc}(\mathrm{invPSh}_q) \times B\mathrm{GL}_1$, where $\mathrm{invPSh}_q(U)$ is a point if $q$ is a unit on $U$ and is empty if not. It carries the line bundle $\ell$ given by the second factor, and `Inv q lineSp` holds.

The code writes $\mathbb{P}(V)$ as the diagonal of the simplicial space `twX E V`, whose term in degree $p$ is $\operatorname{disc}(E_p) \times \mathrm{Fib}_N$ (`twIso`). On each term, `colLine` is the map to $\mathrm{lineSp}$ that sends a point to the unit witness from `Inv q E` and to the line of `Fib.line`. Together these give a map `ellB` from `twX E V` to the constant object $\mathrm{lineSp}$.

1. Choose cocycles $z_j$ on $\mathrm{lineSp}$ with class $c_1(\ell)^j$, for $j < N$.
2. Apply `pbf_of_model` with `ellB`, the $z_j$ and the hypothesis on discrete spaces. It needs two facts:
   - on the diagonal, the class of $z_j$ pulled back along `ellB` is the pullback along `twIso` of $c_1(L)^j$;
   - on each term, the class of $z_j$ pulled back along `colLine` is $c_1$ of `Fib.line` to the power $j$.
3. Both facts follow by rewriting. `pull_cpow` moves pullback inside a cup power, by naturality of cup and of $1$. Naturality of $c_1$ then turns the class into $c_1$ of a composite line bundle. `twIso_line`, `diag_line` and `colLine_line` identify that composite.

The naturality facts are `a6nat_holds`, which proves the four parts of `DivisorNaturality`: for cup, for $1$, for $c_1$ and for Kummer classes.

## In the Lean code

The theorem is in [ProjectiveBundleFormulaOfDiscreteSpaces.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ProjectiveBundleFormulaOfDiscreteSpaces.lean#L65), with `invPSh` at line 12 and `colLine` at line 37. `twX`, `Fib`, `bidiag` and `twIso` are in [SpanRangeMulVecLe.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SpanRangeMulVecLe.lean#L220). `a6nat_holds` is in [CupChernKummerPullbackNaturality.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CupChernKummerPullbackNaturality.lean#L12), and `DivisorNaturality` in [DivisorSupportCondition.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/DivisorSupportCondition.lean#L26). Each part of `a6nat_holds` is a `GlobalTheory.T` lemma that we have not opened.

The cocycles $z_j$ are chosen once, on $\mathrm{lineSp}$, and do not depend on $E$ or $V$. Only the existence of a class representative is used (`mk_surjective`).
