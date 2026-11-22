---
id: e3-main
title: Restriction to the generic fibre, by induction on the number of variables
kind: theorem
decl: UpperTheory.Et.E3.main
module: Development.AutomorphicArithmetic.CommutativeAlgebra.EtaleCohomology.N81
covers: 724
status: drafted
drafted_by: writer@claude
---
This theorem proves the axiom E3 of the étale chapter from 11 other axioms. [The E3 theorem](/entry/etale-base-change-of-duality/) supplies the axioms and is its only user. The proof is an induction on the number of variables of a polynomial ring. Its step, [n8](/entry/n8/), has most of the content.

## Statement

**Theorem.** Assume the axioms A1 to A5, A9, B1, B2, B4, C3 and C4. Let $T$ be an absolutely integrally closed local domain with fraction field $K$, let $q \neq 0$ be a unit in $T$, and let $X \to \operatorname{Spec} T$ be smooth. Then restriction $H^n(X, \mathbb{Z}/q(i)) \to H^n(X_K, \mathbb{Z}/q(i))$ is bijective for all $n$ and $i$.

C3 is the case of the statement for $\operatorname{Spec}$ of an étale algebra over $T[t]$. C4 is homotopy invariance: $\operatorname{Spec} A[t] \to \operatorname{Spec} A$ induces a bijection on $H^*(\,\cdot\,, \mathbb{Z}/q(i))$ when $q$ is a unit in $A$.

## Proof

Call a ring map $g \colon A \to B$ *restrictive* if $\operatorname{Spec} B \to \operatorname{Spec} A$ induces bijections on $H^n(\,\cdot\,, \mathbb{Z}/q(i))$ for all $n$ (`RE`). For $t \colon T \to A$, say that $(K, A)$ is *good* (`Good`) if for every étale $A$-algebra $B$ the map $B \to K \otimes_T B$ is restrictive.

1. **Algebraicity.** The map $k \colon T \to K$ has the property `AlgRes`: each $z = a/b \in K$ is a root of the nonzero polynomial $bX - a$ over $T$. This is proved inline.
2. **Base** (`n5`, from `BasePf.Base_of`). $(K, T)$ is good. It comes from C3 through `n6`, which passes from étale to ind-étale algebras over $T[t]$ by the limit lemma `n7`.
3. **Step** ([n8](/entry/n8/)). If $(K, A)$ is good, then $(K, A[x])$ is good. So $(K, T[x_1, \dots, x_n])$ is good for each $n$, by induction. The isomorphisms $T[x_1, \dots, x_{n+1}] \cong T[x_1, \dots, x_n][x]$ (`finSuccEquiv`) and $T[\,\emptyset\,] \cong T$ are handled by `Good.of_equiv`.
4. **Global** (`n78`, from `GlobalPf.Global_of`). If $(K, T[x_1, \dots, x_n])$ is good for all $n$, then E3 holds for each smooth $X \to \operatorname{Spec} T$. Its inputs are a Zariski-local criterion (`n79`) and two lemmas, `n83` (`Affine`) and `n84` (`LocEt`), which we have not unfolded.

The rest is bookkeeping.

## In the Lean code

The theorem is at [N81.lean line 260](lean:Development/AutomorphicArithmetic/CommutativeAlgebra/EtaleCohomology/N81.lean#L260). The notions `RE`, `BC`, `Good`, `AlgRes`, `Base`, `Step` and `Global` are in [EtaleBaseChangeFractionFieldIndEtaleOverPolynomi.lean](lean:Development/EtaleCohomology/EtaleSheaves/EtaleBaseChangeFractionFieldIndEtaleOverPolynomi.lean#L9).

- The same file has `t_E3Cut.goal_of`, which gives the same induction for the 26 axioms of `EtaleChapterEThree`. `main` repeats that proof with the shorter record `Hyp`, and proves `AlgRes` for $T \to K$ by hand instead of from `AlgResProps`.
- `N81.lean` holds the one-line lemmas `n1` to `n84`, which build the inputs. The file is named after `n81`, a Čech lemma deep inside `n78`.
- The record `Hyp` is only passed down to `n5`, `n8` and `n78`. We have not checked which of the 11 axioms each leaf uses.
