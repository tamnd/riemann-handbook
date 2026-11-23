---
id: lemma-k
title: Lemma K from the odd rank bound and three duality statements
kind: theorem
decl: UpperTheory.V.ZK.lemmaK
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ClassCounting.LemmaKOfLitN
covers: 635
status: drafted
drafted_by: writer@claude
---
This theorem proves Lemma K, the bound on $H^2$ of the [window bound](/proof/vwin/), from four hypotheses: `BOdd`, Poitou-Tate duality, local finiteness and local Tate duality. It feeds 21 proved steps to `lemmaK_of_steps`. Its user [`lemmaK_of_litN_alt`](/entry/lemma-k-of-lit-n-alt/) takes the three duality statements from the literature hypothesis. The rank bound `BOdd` comes from [`bOdd`](/entry/b-odd/).

## Statement

**Theorem.** Assume `BOdd`, `PoitouTateDuality`, `LocalFinitenessK` and `LocalTateDualityK`. Then there is $C_K$ with `LemmaK` $C_K$.

`LemmaK` is stated in [the parent entry](/entry/lemma-k-lit-n-alt/). `BOdd` says: let $L$ be a totally complex number field with $r_2$ complex places, $k$ even with $k + 1 < r_2$, $l \ge 1$ and $n \ge 2(k+1) + 4$. For a class $x \in H_{k+1}(\mathrm{GL}_n(\mathcal{O}_L), \mathbb{Z})$ there is a sequence $z_t(x)$ in the homology of $\mathrm{GL}_{l^t n}(\mathcal{O}_L)$, defined by $z_{t+1} = \psi_l(z_t) - l^{t+2} \operatorname{st}(z_t)$, where $\psi_l$ is the block diagonal map $A \mapsto 1_l \otimes A$ and $\operatorname{st}$ is the stabilization map. Then the $\mathbb{Z}$-span of the classes $z_k(x)$, for all $x$, has rank at most $r_2$.

## Proof

The proof is the one term `lemmaK_of_steps hB hP hF hT` followed by the 21 proved steps. `lemmaK_of_steps` composes them as follows.

1. **Chains.** `SChain`, `SPrism`, `SPrismMul` and `SZc` are facts on bar chains of groups: $\partial^2 = 0$, functoriality, a prism homotopy for conjugation, and that an explicit chain $z_c$ on $\mathbb{Z}/q$ is a cycle. `STrans` and `SCoc` build a cocycle on $k^\times$ for a finite field $k$. Together they give `STheta`: for each finite field there is an additive invariant $\theta$ of chains on $\mathrm{GL}(V)$ with a prescribed value on $z_c$ (the condition `HasVal`).
2. **Classes from Kummer elements.** `SClass` (from `SChain`, `SPrism`, `SPrismMul`, `SZc`, `SRel`, `SEta`, `SStein`) builds, for an element $\alpha$ of a layer $F/L$ of the cyclotomic tower with a divisor condition, a cycle $y$ in the chains of some $\mathrm{GL}_N(\mathcal{O}_L)$ whose value under $\theta$ at each good residue field detects the residue of a norm of $\alpha$.
3. **Upper bound.** `SUpper` (from `SChain` and `BOdd`) bounds the number of such values by $(l^\nu)^{r_2}$ times two orders of torsion subgroups of $H_m(\mathrm{GL}_N(\mathcal{O}_L), \mathbb{Z})$.
4. **Counting.** `SFew` (from `STheta`, `SPhi`, `SClass`, `SUpper`, `SDetect`) bounds the number of such $\alpha$ that are distinct modulo $l^\nu$-th powers. `SDetect` is a detection statement: an element that is an $l^\nu$-th power at enough residue fields is an $l^\nu$-th power. Then `SNum` combines `SFew`, `SCount`, `SSha`, `SLayer` and the torsion bound `STors` into `ShaK` $C$. This is a bound $s \log l \le \exp((2En)^C \log(2D))$, where $s$ is the length of the classes in $H^1(G_L, \mathbb{Q}_l/\mathbb{Z}_l(-E))$ that are trivial on the decomposition groups above $l$ and unramified elsewhere.
5. **From $H^1$ to $H^2$.** `SFinal` turns `ShaK` into `LemmaK` with Poitou-Tate duality, local finiteness and local Tate duality. These are the only places where the three hypotheses enter.

## In the Lean code

The theorem is in [ClassCounting/LemmaKOfLitN.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ClassCounting/LemmaKOfLitN.lean#L28). The step statements and `lemmaK_of_steps` are in [LemmaKOfSteps.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ClassCounting/LemmaKOfSteps.lean#L170). `sFinal` is in [SFinal.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ClassCounting/SFinal.lean#L100) and `sNum` in [NumThree.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ClassCounting/NumThree.lean#L211). We have not opened the proofs of the other steps.

Odd names:

- Five steps (`SRel`, `SStein`, `SDetect`, `SFewOf`, `SLayer`) are proved by theorems that are all named `intersectionNumber_baseChange`, in the namespaces `LateralTheory.Fin.SRel` and so on. No intersection number appears in their statements. Each is a one-line alias, for example `intersectionNumber_baseChange : SRel := relation_statement_holds` in [FinSRel.lean](lean:Development/EtaleCohomology/CyclotomicDiscriminants/FinSRel.lean#L6).
- `SSha` is proved by `PositivityTheory.QuaternionShaBounds.sSha`. No quaternion algebra appears in `SSha`.
