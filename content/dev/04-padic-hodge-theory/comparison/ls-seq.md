---
id: ls-seq
title: The level sequences for crystalline cohomology of a smooth model
kind: theorem
decl: CrystallineSemistableComparison.Pb.LsG.ls_seq
module: Development.WeilBound.CoreStatements.PadicHodgeComparison.EtaleCohomologyComparison.PerfectoidPullbacks.LocalSystemQuotients.LsSeqEq
covers: 332
status: drafted
drafted_by: writer@claude
---
This theorem gives, for a smooth model over $\mathcal{O}_K$, the maps of the long exact sequences that connect the levels $W_m(k)$ of its crystalline cohomology. The lemmas `lw_fin` and `pin_all` use it to show that the limit over $m$ is a finite $W(k)$-module and to bound a cokernel. They lead to the [local steps](/entry/steps-holds/). Below this theorem are 332 declarations.

## Statement

Let $K$ be an extension of $\mathbb{Q}_\ell$ in $\overline{\mathbb{Q}}_\ell$. A *residue datum* $r$ (`Res`) is a perfect field $k$ of characteristic $\ell$, a surjection $\rho \colon \mathcal{O}_K \to k$, and a map $k \to \mathcal{O}^\flat$ that lifts $\rho$. A *model* $M$ is a scheme $X$ over $\mathcal{O}_K$. It is *smooth* (`Sm`) if it is projective, strictly semistable and smooth.

Let $W_m = W(k)/\ell^m$. Let $H^j_m$ (`Wc.HS`) be the degree $j$ cohomology of the nerve complex of the category `Thick` of thickenings over $W_m$ of $X_k$, with reduction maps $H^j_{m+1} \to H^j_m$. We have not unfolded `Thick`.

An `LSeq` from $(H^j_m)$ to $(H^{j+1}_m)$ is three families of maps $\rho_{c,b} \colon H^j_c \to H^j_b$, $\nu_{a,c} \colon H^j_a \to H^j_c$ and $\delta_{b,a} \colon H^j_b \to H^{j+1}_a$, compatible with reduction, such that $\ell^n$ kills $H^j_n$, $\rho_{c,c} = 1$, $\nu_{a,c} \circ \rho_{c,a} = \ell^{c-a}$, and for $c = a + b$, $\ker \rho_{c,b} \subset \operatorname{im} \nu_{a,c}$ and $\ker \delta_{b,a} \subset \operatorname{im} \rho_{c,b}$.

**Theorem.** For a residue datum $r$, a smooth model $M$ and $j \geq 0$, there is an `LSeq` from $(H^j_m)_m$ to $(H^{j+1}_m)_m$.

## Proof

Let $K_m$ (`Kt`) be the same complex on the full subcategory `FlatT` (not unfolded).

1. `seq_flat`. `LsQ.seqflat0_pf` gives maps $\psi_n \colon K_n \to K_{n+1}/\ell^n$, bijective on cohomology and compatible with restriction. By `flat_witt_tower_level`, $K_c$ is `FlatL`: $\ell^c$ kills it, and if $a + b = c$ and $\ell^b x = 0$ then $x \in \ell^a K_c$. Then `quotient_reduction_bijective_of_flat` makes the maps $K_m/\ell^b \to K_{m+1}/\ell^b$ bijective on cohomology.
2. `lseq_of_flat_tower` builds an `LSeq` for the system `tsys`: $H^j(K_n)$, with transitions $\psi_n^{-1}$ after projection.
3. `smooth_model_restriction_bijective`: for a smooth model, restriction $H^j_m \to H^j(K_m)$ is bijective.
4. `lseq_of_level_isos` carries the `LSeq` of step 2 along these isomorphisms.

## In the Lean code

The theorem is in [LsSeqEq.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/LocalSystemQuotients/LsSeqEq.lean#L31), with `seq_flat` at line 21. `LSeq` is in [Tens.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/TwistedRepresentations/Tens.lean#L12), `Wc.HS` in [ResCoeff.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/BocksteinBaseChange/ResCoeff.lean#L140), `Kt` in [ModFSW.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/LocalSystemQuotients/ModFSW.lean#L34), and `FlatL` and `tsys` in [FlatL.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/LocalSystemQuotients/FlatL.lean#L30). The four `GlobalTheory.T` lemmas are wrappers, for example [LseqOfFlatTowerStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LseqOfFlatTowerStatement.lean#L6). Each is `first | exact` of a `GlobalTheory.CompanionTheory` lemma that we have not opened. So the real work of this proof is out of view.

`LSeq` asks for one half of exactness only: kernels lie in images. It does not ask that $\rho_{c,b} \circ \nu_{a,c} = 0$ or $\delta_{b,a} \circ \rho_{c,b} = 0$. The users in [PhiAIter.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/FrobeniusFactorisation/PhiAIter.lean#L40) pass it to more wrappers, such as `module_finite_limit_of_lseq`.
