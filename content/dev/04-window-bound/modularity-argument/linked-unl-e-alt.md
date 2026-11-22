---
id: linked-unl-e-alt
title: The diagonal characters of a lift are not linked, from the modularity inputs
kind: theorem
decl: UpperTheory.Gal.projectedFormsSystemPart.linkedUnlE_alt
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.UnitaryRankTwoFlags
covers: 374
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement $\mathrm{LinkedUnlE}$: for a three-dimensional lift with prescribed inertia characters above $\ell$, no two of the diagonal characters at a place above $\ell$ differ by the cyclotomic character. [VWin from the extended hypotheses](/proof/vwin/) reaches this theorem through `UpperTheory.V.Z.J.linkedUnlE_alt`, which takes the hypotheses from $\mathrm{HypothesesH'}$ (Step 5 of the chapter [The window bound VWin](/proof/vwin/)). Through `unlEnd3E`, [the first count](/entry/count-i-of-printed-bound-k-kato-automorphy/) uses the result to prove the type I admissibility and the first rigidity statement, two inputs of [the bound for one character](/entry/one-char-u-of-kato-two-w-rig-adm-i-automorphy/). The count $\mathrm{CountV}$ uses it too.

## Statement

Fix data as in [the bound for one character](/entry/one-char-u-of-kato-two-w-rig-adm-i-automorphy/): a quadratic character $\eta$, a prime $\ell$, a coefficient ring $\mathcal{O}$, an even level $N$, a weight $e$, a character $\psi$ and $\Psi = \chi_{\mathrm{cyc}}^e\psi$. Fix also a CM field $L$, a frame $\Phi$ of places above $\ell$ with the conditions `Ok` and `Big`, a link datum $k$ and a seed clause. Let $A$ be a discrete valuation ring finite over $\mathcal{O}$. Let $\rho$ be a framed lift of rank 3 over $A$ whose diagonal characters on inertia at each $v \in \Phi$ are $\rho.\psi_{v,i} = \Psi^{w(3,i)}$. Let $r \colon G_L \to \mathrm{GL}_3(\overline{\mathbb{Q}}_\ell)$ come from $\rho$, be irreducible on each open subgroup, and be potentially crystalline at $v$.

**Theorem.** Assume global and local class field theory and the twelve other hypotheses below. Then for all $i, j$ there is $g \in G_v$ with $\rho.\psi_{v,i}(g) \ne \rho.\psi_{v,j}(g)\,\chi_{\mathrm{cyc}}(g)$.

The hypotheses are `ModUAlt`, `ModNAlt`, `LevEx`, `LamEx`, `ProModularRingExists`, `UnitaryThreeAutomorphyDense`, `Seed2Alt`, `Sd.Twist`, `Sd.AlgCyc`, `Sd.AlgRes`, `TanA` and `Th.DenseThresholdMainCase`. We have not unfolded them.

## Proof

The proof is by contradiction. Suppose that $\rho.\psi_{v,i} = \rho.\psi_{v,j}\chi_{\mathrm{cyc}}$ on $G_v$.

1. `openEx2E_alt` uses all hypotheses except `TanA` and `Th.DenseThresholdMainCase`. It builds modular rings of rank 2 and rank 3 with `cRealEx`, seed points with `seedPtOf_alt`, and open subsets with `mod_l_open_existence`. It returns a larger coefficient ring, a rank 3 datum $R$ with an ideal $J$ and a surjection $\varphi$ between two of its algebras, with the properties `AllGood`, `ModularAlt`, `DimT` and `EndPtAlt`.
2. `xiEx` gives a point $\xi$ of $R$ that carries $\rho$ to $r$. `xiTI` and `xiArith` give three properties of $\xi$ and a weight $w$ for it. `xiArith` uses global class field theory.
3. `TanA` turns the linked equality into two tangent vectors $D, D'$ at $\xi$.
4. The proved statement `endJ`, with `unramified_algebraic_weights` and `red2_alt` (which uses `Th.DenseThresholdMainCase`), shows that such tangent vectors cannot exist. This is the contradiction.

## In the Lean code

The theorem is in [UnitaryRankTwoFlags.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/UnitaryRankTwoFlags.lean#L116). It only applies `UnitaryRankTwoFlagsAlt` (line 36) to `openEx2E_alt` (line 62) and to proved inputs. The isomorphism $\overline{\mathbb{Q}}_\ell \cong \mathbb{C}$ comes from `GlobalTheory.nonempty_padicAlgCl_ringEquiv_complex`. $\mathrm{LinkedUnlE}$ is in [LinkedUnlEOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/LinkedUnramifiedChains/LogarithmicNormBounds/LinkedUnlEOf.lean#L12), and its conclusion `UnlPt` is in [AdmissibleUnitaryThreePoint.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/LinkedUnramifiedChains/WeightInfinitesimalCharacters/AdmissibleUnitaryThreePoint.lean#L20). We have not unfolded `XiEx`, `XiTI`, `XiArith`, `TanA`, `End`, `Red2Alt` or the ring structure `CReal`. Two declarations have the name `linkedUnlE_alt`: this one, and `UpperTheory.V.Z.J.linkedUnlE_alt` in [LinkedUnlE.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/LinkedUnlE.lean#L43), which calls it. The names `UnitaryRankTwoFlags` and `projectedFormsSystemPart` do not describe the statement.
