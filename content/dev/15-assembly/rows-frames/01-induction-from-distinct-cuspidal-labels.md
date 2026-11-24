---
title: Induction from distinct cuspidal labels
decls:
  - GlobalTheory.HcIrr.isIrrRep_of_monotone
  - GlobalTheory.T.isIrrRep_harishChandra_distinct_cuspidal_labels
  - GlobalTheory.HcIrr.isIrrRep_hcRep
  - GlobalTheory.T.squarefreeLabel_isCuspidalParabolicProductCharacter
  - GlobalTheory.SqfreeCuspProd.isCuspProdChar_of_squarefree
  - GlobalTheory.GoodFactor.irreducible_character_good_idempotent_cuspidal_product
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Induction from distinct cuspidal labels

This section proves that an irreducible character of a finite product of groups $\mathrm{GL}_r(\mathbb{F}_g)$ that lies in the good idempotent of the third place series is a product of characters of cuspidal parabolic inductions. The result is used by [the nonempty set of hypotheses](/entry/hypotheses-nonempty-of-unramified-exponents-alt/) of the unitary hypotheses chapter, where the characters of a family must have this form before the multiplicity bounds of the next section apply. The proof has three steps. First, Harish-Chandra induction from cuspidal representations with pairwise distinct labels is irreducible. Second, a squarefree label gives distinct labels, so a simple representation with a squarefree label has the character of such an induction. Third, a character in the good idempotent splits as a product of factors with squarefree labels.

We use [parabolic induction](/learn/representations/#parabolic-induction-and-the-jacquet-module) and [cuspidal representations](/learn/representations/#cuspidal-representations-and-segments) of Volume 1. All representations are finite dimensional over $\mathbb{C}$.

Let $k$ be a finite field and $r \geq 1$. A *block function* is a surjective map $b : \{1, \dots, r\} \to \{1, \dots, s\}$. Its blocks are the sets $I_c = b^{-1}(c)$. Let $P_b \subseteq \mathrm{GL}_r(k)$ be the group of matrices $g$ with $g_{ij} = 0$ when $b(i) > b(j)$, and let $L_b = \prod_c \mathrm{GL}(k^{I_c})$ be its Levi quotient. When $b$ is monotone, $P_b$ is a standard block upper triangular parabolic subgroup. For representations $\lambda_c$ of $\mathrm{GL}(k^{I_c})$, let $\sigma_b = \bigotimes_c \lambda_c$, inflated from $L_b$ to $P_b$. The *Harish-Chandra induction* is the representation $R_b(\lambda) = \mathrm{Ind}_{P_b}^{\mathrm{GL}_r(k)} \sigma_b$. We realize it on the space of functions $f : \mathrm{GL}_r(k) \to \bigotimes_c \lambda_c$ with $f(pg) = \sigma_b(p) f(g)$ for $p \in P_b$, with the action by right translation.

A *label map* is a rule $\ell$ that gives each simple cuspidal representation $\sigma$ of a group $\mathrm{GL}_m(k)$, $m \geq 1$, a monic polynomial $\ell(\sigma) \in k[X]$. We ask two things of it: $\ell(\sigma)$ is irreducible, and isomorphic representations of the same group get the same label. A simple representation $\tau$ of $\mathrm{GL}_r(k)$ has *label* $f$ if there are a block function $b$ and simple cuspidal $\lambda_c$ such that $\tau$ is a constituent of $R_b(\lambda)$ and $f = \prod_c \ell(\lambda_c)$. For $\mathrm{GL}_r(\mathbb{F}_q)$ one can take for $\ell(\sigma)$ the minimal polynomial of a regular character of $\mathbb{F}_{q^m}^\times$ attached to $\sigma$, as in the work of Green on the characters of finite general linear groups (Trans. Amer. Math. Soc. 80, 1955). We use only the two properties above.

A *cuspidal datum* for a monotone $b$ is a representation $\sigma$ of $P_b$ such that $\sigma$ is irreducible, the unipotent radical of $P_b$ acts trivially, and no nonzero vector is fixed by the unipotent radical of a proper block parabolic inside one block. Two blocks $c \neq c'$ carry the *same factor* if they have the same size and the factors of $\sigma$ at $c$ and $c'$ are isomorphic. The datum has *distinct factors* if no two distinct blocks carry the same factor. We use the following theorem, which is proved apart from this chapter: the induction of a cuspidal datum with distinct factors is irreducible. This is the case of trivial ramification group in the theory of Howlett and Lehrer (Invent. Math. 58, 1980).

**Lemma 7.1.1 (Monotone blocks).** Let $b$ be a monotone block function and let $\lambda_c$ be simple cuspidal representations of $\mathrm{GL}(k^{I_c})$ with pairwise distinct labels $\ell(\lambda_c)$. Then $R_b(\lambda)$ is irreducible.

Lean: `GlobalTheory.HcIrr.isIrrRep_of_monotone`.

*Proof.* We check that $\sigma_b$ is a cuspidal datum. It is monotone by assumption. The tensor product of simple representations of the factors of $L_b$ is a simple representation of $L_b$. Let $p$ lie in the unipotent radical. Then each diagonal block of $p$ is the identity, so the image of $p$ in each factor $\mathrm{GL}(k^{I_c})$ is $1$, and $p$ acts as the identity. A vector of $\bigotimes_c \lambda_c$ fixed by the unipotent radical of a proper block parabolic inside one block would give a fixed vector in a cuspidal factor, so it is zero.

Next we show that the factors are distinct. Let $c \neq c'$ be blocks with the same size $d$ and isomorphic factors. Each factor is identified with a representation of $\mathrm{GL}_d(k)$ by a choice of order on its block. The isomorphism of the factors then gives an isomorphism of these representations of $\mathrm{GL}_d(k)$, so $\ell(\lambda_c) = \ell(\lambda_{c'})$. The labels are distinct, so $c = c'$, a contradiction. The theorem on cuspidal data with distinct factors now shows that the induction of $\sigma_b$ is irreducible. The space of $R_b(\lambda)$ is the same as the space of this induction, since both are defined by the same group $P_b$. So $R_b(\lambda)$ is irreducible. $\square$

**Theorem 7.1.2 (Distinct cuspidal labels).** Let $b$ be a block function and let $\lambda_c$ be simple cuspidal representations of $\mathrm{GL}(k^{I_c})$ such that $c \mapsto \ell(\lambda_c)$ is injective. Then $R_b(\lambda)$ is irreducible.

Lean: `GlobalTheory.T.isIrrRep_harishChandra_distinct_cuspidal_labels` (also `GlobalTheory.HcIrr.isIrrRep_hcRep`).

*Proof.* Order the blocks by their least element. This gives a permutation $w$ of $\{1, \dots, r\}$ and a monotone block function $b'$ with $b' = \pi \circ b \circ w^{-1}$ for a permutation $\pi$ of the blocks. Conjugation by the permutation matrix of $w$ maps $P_b$ to $P_{b'}$ and identifies each block of $b$ with a block of $b'$. Transport the $\lambda_c$ along these identifications to get $\lambda'_{c'}$. The labels do not change, so $c' \mapsto \ell(\lambda'_{c'})$ is still injective. The lemma gives that $R_{b'}(\lambda')$ is irreducible. Conjugation by $w$ is an isomorphism from $R_{b'}(\lambda')$ to $R_b(\lambda)$ that is compatible with the group action, so $R_b(\lambda)$ is irreducible. $\square$

A function $\theta$ on $\mathrm{GL}_r(k)$ is a *cuspidal parabolic product character* if it is the character of $R_b(\lambda)$ for a monotone $b$ and simple cuspidal $\lambda_c$.

**Theorem 7.1.3 (Squarefree labels).** Let $\tau$ be a simple representation of $\mathrm{GL}_r(k)$ with label $f$, and let $f$ be squarefree. Then the character of $\tau$ is a cuspidal parabolic product character.

Lean: `GlobalTheory.T.squarefreeLabel_isCuspidalParabolicProductCharacter` (also `GlobalTheory.SqfreeCuspProd.isCuspProdChar_of_squarefree`).

*Proof.* Take $b$ and $\lambda_c$ with $\tau$ a constituent of $R_b(\lambda)$ and $f = \prod_c \ell(\lambda_c)$. Each block is nonempty, so each $\ell(\lambda_c)$ is irreducible. Let $c \neq c'$ with $\ell(\lambda_c) = \ell(\lambda_{c'}) = h$. Then $h^2$ divides $f$. Since $f$ is squarefree, $h$ is a unit, which is false for an irreducible $h$. So $c \mapsto \ell(\lambda_c)$ is injective. The last theorem gives that $R_b(\lambda)$ is irreducible. A simple constituent of an irreducible representation is isomorphic to it, so the character of $\tau$ is the character of $R_b(\lambda)$.

It remains to make $b$ monotone. Reorder the blocks as in the proof of the last theorem. This gives a monotone $b'$ and $\lambda'$ such that $R_{b'}(\lambda')$ and $R_b(\lambda)$ have the same character. So the character of $\tau$ is the character of $R_{b'}(\lambda')$, which is a cuspidal parabolic product character. $\square$

Now we come to the family of the third place series. Fix a host with two primes $g_1, g_2$, and for each $k \in \{1, 2\}$ a finite set $\mathrm{Pl}_k$ of places over $g_k$. Put
$$G_0 = \prod_{k = 1}^{2} \prod_{v \in \mathrm{Pl}_k} \mathrm{GL}_r(\mathbb{F}_{g_k}).$$
For each $k$ there is a family of central idempotents $e_k(f)$ of $\mathbb{C}[\mathrm{GL}_r(\mathbb{F}_{g_k})]$, the *series idempotents*, indexed by monic polynomials $f$ of degree $r$. A tuple $(f_{k,v})$ of such polynomials is *good* if each $f_{k,v}$ is squarefree and some further conditions of the family hold. The *good idempotent* is
$$e_0 = \sum_{(f_{k,v}) \text{ good}} \ \bigotimes_{k, v} e_k(f_{k,v}).$$
An irreducible character $\chi$ of $G_0$ *lies in* $e_0$ if $\sum_g e_0(g) \chi(g) = \chi(1)$.

**Theorem 7.1.4 (Good characters are cuspidal products).** Assume that for each $k$ there is a label map $\ell_k$ for $\mathrm{GL}_r(\mathbb{F}_{g_k})$ such that $e_k(f)$ is the sum of the central idempotents of the simple representations with label $f$, for all $f$. Let $\chi$ be an irreducible character of $G_0$ that lies in $e_0$. Then there are cuspidal parabolic product characters $\theta_{k,v}$ of $\mathrm{GL}_r(\mathbb{F}_{g_k})$ with
$$\chi\big((x_{k,v})\big) = \prod_{k, v} \theta_{k,v}(x_{k,v})$$
for all $(x_{k,v}) \in G_0$.

Lean: `GlobalTheory.GoodFactor.irreducible_character_good_idempotent_cuspidal_product`.

*Proof.* An irreducible character of a finite product of groups is a product of irreducible characters $\psi_{k,v}$ of the factors. The idempotents $e_k(f)$ are central and orthogonal for distinct $f$, so $\chi$ lies in exactly one term of $e_0$. This gives a good tuple $(f_{k,v})$ such that $\psi_{k,v}$ lies in $e_k(f_{k,v})$ for each $(k, v)$. By the assumption on the label maps, $\psi_{k,v}$ is the character of a simple representation $\tau_{k,v}$ with label $f_{k,v}$. The tuple is good, so $f_{k,v}$ is squarefree. The theorem on squarefree labels shows that $\psi_{k,v}$ is a cuspidal parabolic product character. Put $\theta_{k,v} = \psi_{k,v}$. $\square$

**Remark 7.1.5 (Formalization).** The induction $R_b(\lambda)$ is `hcRep` on the space `hcSpace`, and the label is `HasLabelO`. The theorem on cuspidal data with distinct factors is `FinGL.IrrProduct.irrPar`, used through `CuspFactor.irrPar_iff_cuspidalProduct`; we read its statement, not its proof. The induced space of `hcRep` is defined by a group of block matrices that is equal to the block parabolic used by that theorem, but not by definition, so the proof of the lemma builds an explicit linear equivalence between the two spaces with `blockTri_le_parab` and `parab_le_blockTri` ([IsIrrRepHarishChandraDistinctCuspidalLabels.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsIrrRepHarishChandraDistinctCuspidalLabels.lean#L52)). The reordering of blocks is `exists_sorted` at line 64 of that file and `T.exists_monotone_blocks_same_harishChandra_character` in the proof of the squarefree theorem. The squarefree theorem proves irreducibility for the unsorted $b$ and then sorts again, so the sorting is done twice. The splitting into factors of a product group is `exists_good_factor`, and the step from a series idempotent to a simple representation with a label is `T.exists_simple_label_of_seriesIdempotent_pair`. The good tuples are `NTypes.goodTuple`; the proof uses only that their entries are squarefree.
