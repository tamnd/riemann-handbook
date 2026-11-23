---
title: A birational group law
decls:
  - GlobalTheory.T.exists_weakNeronModel_birational_groupLaw
  - GlobalTheory.SS.NeutralModel.exists_birLaw
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A birational group law

Let $R$ be a strictly Henselian discrete valuation ring with fraction field $K$, and let $A$ be a commutative abelian scheme over $K$. In this section we prove that a weak Néron model of $A$ with irreducible members contains one member $N$ with a birational group law: the shears and the inverse of $A$ are generic isomorphisms of $N$. There is also an integer $c \geq 1$ such that translation by $a^c$ is a generic isomorphism of $N$ for every rational point $a$. The proof uses [the permuted members](/entry/exists-automorphism-permutation-max-order-members/) of the last section. The result is the second step of [the neutral group model](/entry/exists-neutral-group-model/). We keep the notation of the last section.

### Shears and group laws

For a group scheme $A$ over $K$ and a $K$-point $a$, let $\tau_a$ be the translation $x \mapsto a x$. The *shears* of $A$ are the automorphisms $(x, y) \mapsto (x, xy)$ and $(x, y) \mapsto (x, x^{-1} y)$ of $A \times A$.

**Definition 6.16.1 (Birational group law).** A model $M$ of $A$ has a *birational group law* if $M$ is irreducible, both shears are generic isomorphisms from $M \times M$ to itself, and the inverse $x \mapsto x^{-1}$ is a generic isomorphism from $M$ to itself.

Lean: `GlobalTheory.SS.BirLaw` (also `GlobalTheory.SS.transl`, translations; `GlobalTheory.SS.shear`, shears).

### One more input

We use the next result, for $R$ strictly Henselian.

**Theorem 6.16.2 (Generic isomorphisms of products).** Let $M$, $M'$, $N$ and $N'$ be irreducible models of $A$, $A'$, $B$ and $B'$, with $A$ and $A \times B$ integral. Let $f : A \cong A'$ and let $\Theta : A \times B \to A' \times B'$ have first component $f \circ \mathrm{pr}_1$. If $\Theta$ is a generic isomorphism from $M \times N$ to $M' \times N'$, then $f$ is a generic isomorphism from $M$ to $M'$.

Lean: `GlobalTheory.T.generic_isomorphism_product_models`.

### The proof

**Lemma 6.16.3 (Idempotents).** Let $S$ be a nonempty finite set with an equivalence relation $\sim$ and a relation $T(i, j, k)$. Assume that for all $i, j$ there is $k$ with $T(i, j, k)$, that $T(i, j, k)$ and $k \sim k'$ give $T(i, j, k')$, and that $T(i, j, k)$, $T(k, l, m)$, $T(j, l, p)$ and $T(i, p, q)$ give $m \sim q$. Then there is $e$ with $T(e, e, e)$.

Lean: `GlobalTheory.SS.NeutralModel.exists_idem_of_rel`.

*Proof.* Choose $k = f(i, j)$ for each pair. On fixed representatives of the classes of $\sim$, let the product of two classes be the class of $f$ of the representatives. The last hypothesis makes this product associative. A finite nonempty semigroup has an idempotent class, and its representative $e$ has $T(e, e, f(e, e))$ with $f(e, e) \sim e$, so $T(e, e, e)$ holds. $\square$

**Lemma 6.16.4 (A power fixes each member).** Let $S$ be a finite set and let $T(p, i, j)$ be relations for $p \in \mathbb{N}$. Assume that each $i$ has $j$ with $T(1, i, j)$, that $T(0, i, i)$ holds, that $T(p, i, j)$ and $T(q, j, k)$ give $T(p + q, i, k)$, and that $T(p, i, j)$ and $T(p + d, i, j)$ give $T(d, i, i)$. Then $T(|S|!, i, i)$ holds for every $i$.

Lean: `GlobalTheory.SS.NeutralModel.rel_factorial`.

*Proof.* Choose $\sigma(i)$ with $T(1, i, \sigma(i))$. By induction $T(p, i, \sigma^p(i))$. Among the $|S| + 1$ points $\sigma^p(i)$ with $p \leq |S|$, two are equal, say for $p < q$. Then $T(p, i, j)$ and $T(q, i, j)$ hold for $j = \sigma^p(i)$, so $T(q - p, i, i)$ holds. Since $1 \leq q - p \leq |S|$, the number $q - p$ divides $|S|!$, and adding $T(q - p, i, i)$ to itself gives $T(|S|!, i, i)$. $\square$

**Theorem 6.16.5 (Birational group law).** Let $R$ be strictly Henselian with fraction field $K$, let $A$ be a commutative abelian scheme over $K$, and let $(M_i)_{i \leq n}$ be a weak Néron model of irreducible models. Then there are a model $N$ of $A$ with a birational group law and an integer $c \geq 1$ such that, for every $K$-point $a$ of $A$, the translation $\tau_{a^c}$ is a generic isomorphism from $N$ to $N$.

Lean: `GlobalTheory.T.exists_weakNeronModel_birational_groupLaw` (also `GlobalTheory.SS.NeutralModel.exists_birLaw`, a second name).

*Proof.* The schemes $A$, $A \times A$ and $A \times A \times A$ are integral. Let $S$ be the set of the theorem on permuted members. For $i, j \in S$ write $i \sim j$ if the identity is a generic isomorphism from $M_i$ to $M_j$. By the calculus of generic isomorphisms this is an equivalence relation. Let $T(i, j, k)$ say that the first shear is a generic isomorphism from $M_i \times M_j$ to $M_i \times M_k$.

We check the hypotheses of the lemma on idempotents. For $i, j \in S$, the theorem on permuted members gives $i', k \in S$ such that the shear is a generic isomorphism from $M_i \times M_j$ to $M_{i'} \times M_k$. The shear keeps the first coordinate, so the theorem on generic isomorphisms of products gives $i \sim i'$, and composing with the product of the inverse of this identity with the identity of $M_k$ gives $T(i, j, k)$. The second hypothesis follows by composing with an identity. For the third, let $\mathrm{sh}$ be the first shear and $s$ the swap. Built from $\mathrm{sh} \times 1$, $1 \times (s \circ \mathrm{sh})$ and associativity, one composite sends $(x, y, z)$ to $(xyz, xy, x)$. Built from $1 \times (s \circ \mathrm{sh})$, $(s \circ \mathrm{sh}) \times 1$ and associativity, another sends it to $(xyz, x, y)$. The four relations and the calculus make the first composite a generic isomorphism from $(M_i \times M_j) \times M_l$ to $M_m \times (M_k \times M_i)$, and the second one from the same model to $M_q \times (M_i \times M_j)$. Both have first coordinate $xyz$. So the second composite after the inverse of the first is a generic isomorphism from $M_m \times (M_k \times M_i)$ to $M_q \times (M_i \times M_j)$ whose first coordinate is the first projection, and the theorem on generic isomorphisms of products gives $m \sim q$.

So there is $e \in S$ with $T(e, e, e)$, and $N = M_e$ is irreducible. The first shear is a generic isomorphism of $N \times N$, and by the calculus so is its inverse, the second shear. The composite $s \circ \mathrm{sh}^{-1} \circ s \circ \mathrm{sh} \circ s$ sends $(x, y)$ to $(x^{-1}, yx)$, so its first coordinate is the inverse. It is a generic isomorphism of $N \times N$, and the theorem on generic isomorphisms of products shows that the inverse is a generic isomorphism of $N$. So $N$ has a birational group law.

Let $a$ be a $K$-point and let $T(p, i, j)$ say that $\tau_{a^p}$ is a generic isomorphism from $M_i$ to $M_j$. Property 1 of $S$ for $\tau_a$ gives the first hypothesis of the lemma on powers. Since $\tau_1 = 1$ and $\tau_{a^p} \tau_{a^q} = \tau_{a^{p+q}}$, the calculus gives the other three. The lemma gives $T(c, e, e)$ with $c = |S|!$, which does not depend on $a$. $\square$

**Remark 6.16.6 (Formalization).** The theorem is proved in [ExistsWeakNeronModelBirationalGroupLaw.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/ExistsWeakNeronModelBirationalGroupLaw.lean#L116); the two lemmas are at lines 18 and 40 of that file. The first name is a `first | exact ...` wrapper in the file with the suffix `Statement`. The definitions are in [OfDerivationFnOn.lean](lean:Development/AbelianVarietyTheory/Definitions/Degenerations/OfDerivationFnOn.lean#L91). The theorem asks for the index set to be $\{1, \dots, n\}$, though only finiteness is used. The commutativity of $A$ is used for $\tau_{a^p} \tau_{a^q} = \tau_{a^{p+q}}$. The idempotent comes from the theorem that a compact semigroup has an idempotent, applied with the discrete topology. The model $N$ is one of the given members $M_e$, though the statement only asks for some model. We did not unfold the inputs.
