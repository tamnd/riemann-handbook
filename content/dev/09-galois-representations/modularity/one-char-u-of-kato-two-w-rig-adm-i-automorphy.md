---
id: one-char-u-of-kato-two-w-rig-adm-i-automorphy
title: The bound for one character, from the Selmer, rigidity and automorphy inputs
kind: theorem
decl: UpperTheory.V.Z.J.oneCharU_of_katoTwoW_rig_admI_automorphy
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.FOneCharU
covers: 438
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{OneCharU}$: for one Dirichlet character $\psi$, a Selmer type length is finite and bounded by valuations of trace differences of three-dimensional Galois representations. [The first count from the printed bound](/entry/count-i-of-printed-bound-k-kato-automorphy/) uses it to get $\mathrm{CountI}$ (Step 5 of the chapter [The window bound VWin](/proof/vwin/)). The proof only reduces to coefficients with ramification index 1, the case of [the bound with unramified coefficients](/entry/one-char-unram-u/), which has the real content.

## Statement

Let $K$ be an imaginary quadratic field, $\ell$ a prime, $\mathcal{O}$ the ring of integers of a finite extension of $\mathbb{Q}_\ell$, $N$ an even level, $e \ge 1$, and $\psi$ a Dirichlet character modulo $N$ with values in $\mathcal{O}$. Let $\Psi = \chi_{\mathrm{cyc}}^{e}\psi$ as a character of $G_{\mathbb{Q}}$. The hypothesis $\mathrm{GD}$ collects the conditions: $\ell \ne 2$, $\ell$ prime to the order of $\psi$ and to $|d_K| h_K$, $\psi(-1) = (-1)^e$, $d_K$ prime to $N$, $(\ell - 1) \nmid 2e$, and some more. Let $V \in \mathbb{N} \cup \{\infty\}$ be the length of the module $\mathrm{Sha}$ of the twist of $\mathbb{Q}_\ell/\mathbb{Z}_\ell$ by $\psi^{-1}\chi_{\mathrm{cyc}}^{-e}$, and let $V_n = V / e_{\mathcal{O}}$, where $e_{\mathcal{O}}$ is the ramification index of $\mathcal{O}$. For $x \in \overline{\mathbb{Q}}_\ell$ put $v_\ell(x) = -\log_\ell |x|$.

**Theorem.** Assume $\mathrm{CohInp}$, $\mathrm{LemmaM}$, $\mathrm{LemmaM'}$, $\mathrm{LemmaP}$, $\mathrm{KatoTwoW}$, the two rigidity statements, $\mathrm{AdmI}$ and $\mathrm{AutomorphyUnramifiedCoefficientsAlt}$. Let the data satisfy $\mathrm{GD}$, fix $\iota \colon \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$ and $\sigma \in G_K$, and put $t = \Psi(\sigma) + 1 + \Psi(\sigma)^{-1}$. Suppose that $\operatorname{tr}\rho(\sigma) \ne t$ for each admissible $\rho \colon G_K \to \mathrm{GL}_3(\overline{\mathbb{Q}}_\ell)$. Then $V < \infty$, and there is a finite set $X$ of pairwise non-isomorphic admissible $\rho$ with
$$V_n \le 2 \sum_{\rho \in X} v_\ell\bigl(\operatorname{tr}\rho(\sigma) - t\bigr).$$

Here $\rho$ is admissible if it is of type I (irreducible, conjugate self-dual automorphic after a twist by $\chi_{\mathrm{cyc}}^{-1}$, of level $N$ and weights $(e, 0, -e)$, with unlinked characters above $\ell$) or of type II (built from the two-dimensional representation of a newform of weight $2e+1$ and level $N|d_K|$, with a $1$ in the middle). The number $t$ is the trace of $\sigma$ on the reducible representation $\Psi \oplus 1 \oplus \Psi^{-1}$.

## Proof

1. `exists_unram` gives a second coefficient ring $\mathcal{O}'$ with $e_{\mathcal{O}'} = 1$ and a character $\psi'$ with values in $\mathcal{O}'$ that has the same values as $\psi$ in $\overline{\mathbb{Q}}_\ell$.
2. `gd_chHom` moves $\mathrm{GD}$ to $\psi'$.
3. `UpperTheory.V.HV.coefIndep` shows that the condition $V = \infty$ and the number $V_n$ do not change. The number $t$ does not change either, since $\Psi$ has the same values.
4. [The bound with unramified coefficients](/entry/one-char-unram-u/) applies to $\psi'$ and gives $X$.

## In the Lean code

The theorem is in [FOneCharU.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/FOneCharU.lean#L75). $\mathrm{OneCharU}$ is `OneCharU_s` in [NumberU3US.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/NumberU3US.lean#L49), and $\mathrm{GD}$ is `GD` in [Counts.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/Counts.lean#L9). `coefIndep` is in [CoefIndep.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/CoefIndep.lean#L68). `exists_unram` and `gd_chHom` are private lemmas. At least four files have private lemmas with these names, for example [OneCharOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/OneCharOf.lean#L64); we have not checked which one the proof reaches. We have not unfolded the condition on $\eta$ in $\mathrm{GD}$. The nine hypotheses only pass to the unramified case.
