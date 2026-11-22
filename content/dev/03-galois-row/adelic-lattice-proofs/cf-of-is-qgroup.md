---
id: cf-of-is-qgroup
title: Finitely many double cosets for a rational subgroup of SL
kind: theorem
decl: GlobalTheory.ClassFin.cf_of_isQGroup
module: Development.AbelianVarietyTheory.Proofs.AdelicLatticeProofs.FiniteAdelicDoubleCosetsOfRationalSLSubgroup
covers: 386
status: drafted
drafted_by: writer@claude
---
This theorem proves a finiteness of double cosets $\Gamma(\mathbb{Q}) \backslash \Gamma(R) / \Gamma(R_0)$ for a rational algebraic subgroup $\Gamma$ of $\mathrm{SL}_\iota$ and an abstract pair $(R, R_0)$ that behaves like $(\mathbb{A}_f, \widehat{\mathbb{Z}})$. Its second name is [finiteAdelicDoubleCosets_of_rational_SL_subgroup](/entry/finite-adelic-double-cosets-of-rational-sl-subgroup/), and [classFinite_integralLevel](/entry/class-finite-integral-level/) uses it through that name. The proof is an induction that reduces the general case to the completely reducible case. Below it are 386 declarations.

## Statement

The objects are in [the entry of the second name](/entry/finite-adelic-double-cosets-of-rational-sl-subgroup/). In short: `IsQGroup Γ` says that $\Gamma \subseteq \mathrm{SL}_\iota(\mathbb{C})$ is a subgroup, stable under $\mathrm{Aut}(\mathbb{C})$ and closed in the $\mathbb{Q}$-Zariski topology. `AdelicPair R R₀` says that $\mathbb{Q} \cap R_0 = \mathbb{Z}$ and $R = \mathbb{Q} + M R_0$ for each $M \geq 1$. For a $\mathbb{Q}$-algebra $A$, $\Gamma(A)$ is the set of matrices over $A$ that satisfy each rational polynomial equation of $\Gamma$ (the Lean `pts Γ A`).

**Theorem.** If `IsQGroup Γ` and `AdelicPair R R₀`, then there is a finite set $T \subseteq \Gamma(R)$ such that each $x \in \Gamma(R)$ is $x = \gamma s u$ with $\gamma \in \Gamma(\mathbb{Q})$, $s \in T$, and $u \in \Gamma(R)$ with entries in $R_0$.

For $R = \mathbb{A}_f$ and $R_0 = \widehat{\mathbb{Z}}$ this has the form of the finiteness of class numbers of Borel (A. Borel, Some finiteness properties of adele groups over number fields, Publ. Math. IHÉS 16, 1963). The Lean statement does not mention adeles.

## Proof

Strong induction on $n = \dim_{\mathbb{C}} \operatorname{span}_{\mathbb{C}} \Gamma$.

1. If $\Gamma$ is completely reducible on $\mathbb{C}^\iota$ (`SS Γ`: each $\Gamma$-stable subspace has a $\Gamma$-stable complement), the result is `classFiniteness_completelyReducible`.
2. If not, `exists_rat_idempotent_blockDiagPart_kills_span` gives a rational idempotent $e$ with $(1 - e) g e = 0$ for each $g \in \Gamma$, so that the image of $e$ is $\Gamma$-stable. It also gives $a \neq 0$ in $\operatorname{span} \Gamma$ with $\mathrm{blk}_e(a) = 0$, where $\mathrm{blk}_e(g) = e g e + (1 - e) g (1 - e)$ is the block diagonal part.
3. `isAutStableSLMatrixGroup_image_blockDiagPart` shows that $\mathrm{blk}_e(\Gamma)$ is again a subgroup of $\mathrm{SL}_\iota(\mathbb{C})$ stable under $\mathrm{Aut}(\mathbb{C})$. `ratZariskiClosure_of_autStable_SL_group` shows that its $\mathbb{Q}$-Zariski closure $\Delta$ satisfies `IsQGroup`, with the same rational equations and the same span.
4. `finrank_span_blockDiagPart_image_lt` uses $a$ to show that $\operatorname{span} \mathrm{blk}_e(\Gamma)$ has dimension less than $n$. So the induction hypothesis gives the result for $\Delta$.
5. The property `CF` depends only on the rational equations of the set (`cf_congr_of_vanI_eq`, in the same file). So it holds for $\mathrm{blk}_e(\Gamma)$.
6. `hasFiniteAdelicDoubleCosets_of_blockDiagPart_image` lifts `CF` from $\mathrm{blk}_e(\Gamma)$ to $\Gamma$.

We have not opened the proofs of the six lemmas `GlobalTheory.T.*`. Steps 1 and 6 do the work: the reductive case and the passage through the kernel of $\mathrm{blk}_e$.

## In the Lean code

The theorem is in [FiniteAdelicDoubleCosetsOfRationalSLSubgroup.lean](lean:Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs/FiniteAdelicDoubleCosetsOfRationalSLSubgroup.lean#L23), and `cf_congr_of_vanI_eq` is at [line 14](lean:Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs/FiniteAdelicDoubleCosetsOfRationalSLSubgroup.lean#L14). The definitions `IsPre`, `IsQGroup`, `SS`, `AdelicPair`, `CF` and `blk` are in [AdelicPair.lean](lean:Development/AbelianVarietyTheory/Definitions/AdelicHermitianForms/AdelicPair.lean#L20). The lemmas it calls:

- `classFiniteness_completelyReducible`, the case `SS Γ`.
- `exists_rat_idempotent_blockDiagPart_kills_span`, `isAutStableSLMatrixGroup_image_blockDiagPart`, `ratZariskiClosure_of_autStable_SL_group`, `finrank_span_blockDiagPart_image_lt`, `hasFiniteAdelicDoubleCosets_of_blockDiagPart_image`, the reduction.

`CF` asks only that the entries of $u$ lie in $R_0$, not those of $u^{-1}$. Since $\det u = 1$, $u^{-1}$ is the adjugate of $u$, so its entries are also in $R_0$. The parent gets the integrality of $u^{-1}$ through `glFreeAlgebraEmb_integral_and_rational`, which we have not opened. The induction is on the dimension of the complex span of $\Gamma$, not on the dimension of the group.
