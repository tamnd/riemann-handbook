---
title: Descent of integral models along an unramified extension
decls:
  - UpperTheory.Lit.Nos.C3.exists_compatible_projective_embeddings
  - UpperTheory.Lit.Nos.C4.exists_scheme_model_descent_unramified
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Descent of integral models along an unramified extension

Let $R \to W$ be an unramified extension of discrete valuation rings, and let $A$ be an abelian variety over the fraction field $K$ of $R$ which acquires good reduction over $W$. This section shows that, under a condition on the residue fields, the abelian scheme over $W$ comes from a scheme $X$ over $R$ whose generic fibre is $A$. The method is classical: embed $A$ and the model over $W$ in one projective space over $R$, compatibly, and take the closure of $A$. In [the next section](/entry/has-good-reduction-of-inertia-fixed/) the result is applied to the inertia fixed field of a separable closure of $K$, and it is the main step of the proof that unramified torsion gives good reduction.

### The descent setting

**Definition 3.2.1 (Unramified descent setting).** An *unramified descent setting* consists of the following data.

1. Discrete valuation rings $R$ and $W$ with fraction fields $K$ and $K'$, a field extension $K \to K'$ and an injective local homomorphism $R \to W$, compatible with the inclusions in $K$ and $K'$.
2. The extension is *unramified*: $\mathfrak{m}_R W = \mathfrak{m}_W$.
3. A set $D$ of automorphisms of $K'$ over $K$ such that $\sigma(W) \subseteq W$ and $\sigma^{-1}(W) \subseteq W$ for each $\sigma \in D$.
4. The *residue condition*: if $x \in W$ and $\sigma(x) - x \in \mathfrak{m}_W$ for every $\sigma \in D$, then there is $r \in R$ with $x - r \in \mathfrak{m}_W$.
5. An abelian variety $A$ over $K$, an abelian scheme $G$ over $W$, and an isomorphism of group schemes $e : G \times_W K' \to A \times_K K'$.

Each $\sigma \in D$ then restricts to an automorphism of $W$ and induces an automorphism $\bar\sigma$ of the residue field $\kappa(W)$. The residue condition says that the elements of $\kappa(W)$ fixed by all $\bar\sigma$ lie in the image of $\kappa(R)$. When $D$ is a group and $\kappa(W)$ is a Galois extension of $\kappa(R)$ with Galois group the image of $D$, this is the main theorem of Galois theory.

**Definition 3.2.2 (Descent datum on the model).** In an unramified descent setting, a *descent datum on $G$* is, for each $\sigma \in D$, a ring automorphism $\tau$ of $W$ with $\sigma|_W = \tau$, and a morphism $\varphi_\sigma : G \to G$ over $\operatorname{Spec}(\tau)$, whose restriction to the generic fibre is $e^{-1} \circ (1_A \times \operatorname{Spec} \sigma) \circ e$.

The morphism $1_A \times \operatorname{Spec}\sigma$ is the automorphism of $A \times_K K'$ which acts on the second factor, and the condition says that $\varphi_\sigma$ extends its transport to $G \times_W K'$.

**Lemma 3.2.3 (Existence of the descent datum).** In an unramified descent setting, a descent datum on $G$ exists.

Lean: `GlobalTheory.T.galois_descent_integral_structure`.

*Proof.* This is the Néron mapping property. By Volume 1, [the abelian scheme $G$ is the Néron model of its generic fibre](/learn/abelian-varieties/#neron-models-and-good-reduction). Let $\tau = \sigma|_W$ and let $G^\tau$ be the base change of $G$ along $\operatorname{Spec}(\tau)$. The transported automorphism of $A \times_K K'$ gives a $K'$-morphism from the generic fibre of $G$ to that of $G^\tau$. The abelian scheme $G^\tau$ is the Néron model of its generic fibre and $G$ is smooth over $W$, so this morphism extends uniquely to a $W$-morphism $G \to G^\tau$. Composing with the projection $G^\tau \to G$ gives $\varphi_\sigma$. $\square$

### Very ample families and matrices

**Definition 3.2.4 (Very ample family of sections).** Let $X$ be a scheme over a ring $B$, $\mathcal{L}$ a line bundle on $X$, and $s_0, \ldots, s_N$ global sections of $\mathcal{L}$. The family is *very ample* if the open sets $X_{s_i}$ where $s_i$ does not vanish cover $X$, each $X_{s_i}$ is affine, and the ring of functions of $X_{s_i}$ is generated over $B$ by the ratios $s_j/s_i$.

A very ample family gives a morphism $X \to \mathbb{P}^N_B$, $x \mapsto (s_0(x) : \cdots : s_N(x))$, and on each $X_{s_i}$ it is a closed immersion into the standard affine chart. If $X$ is separated over $B$, the morphism is a closed immersion.

**Lemma 3.2.5 (Linear change).** Let $(s_j)$ be a very ample family of sections of $\mathcal{L}$ over $B$, and let $k \in M_{N+1}(B)$ have invertible determinant. Then the family $s'_j = \sum_m k_{jm} s_m$ is very ample.

Lean: `GlobalTheory.T.isVeryAmpleBySections_of_invertible_linear_change`.

*Proof.* The matrix $k$ defines an automorphism of $\mathbb{P}^N_B$, and the morphism given by $(s'_j)$ is the composite of that given by $(s_j)$ with this automorphism. $\square$

**Lemma 3.2.6 (A stable matrix).** In an unramified descent setting with a descent datum on $G$, there are an integer $N$, a line bundle $\mathcal{H}$ on $A$ with a very ample family $s_0, \ldots, s_N$, a line bundle $\mathcal{M}$ on $G$ with a very ample family $t_0, \ldots, t_N$, an isomorphism $w$ of the pullbacks of $\mathcal{M}$ and $\mathcal{H}$ to $G \times_W K'$, and a matrix $g \in M_{N+1}(K')$ with invertible determinant, such that the following hold.

1. Under $w$ and $e$, $t_j = \sum_k g_{jk} s_k$ on $G \times_W K'$ for each $j$.
2. For each $\sigma \in D$ there is $h_\sigma \in M_{N+1}(W)$ with $\sigma(g) = h_\sigma g$, where $\sigma$ acts on the entries.

Lean: `UpperTheory.Lit.Nos.C2.exists_veryAmple_families_stable_matrix`.

*Proof.* We give the steps. The abelian variety $A$ is projective, so it has an ample line bundle $\mathcal{H}_0$ with a very ample family. The pullback of $\mathcal{H}_0$ to the generic fibre of $G$ extends to a line bundle $\mathcal{M}_0$ on $G$, since $G$ is regular. A power $\mathcal{M}_0^{n}$ is very ample over $W$, and it has a very ample family $t_0, \ldots, t_N$ which is a basis of its global sections over $W$. Put $\mathcal{H} = \mathcal{H}_0^{n}$ and $\mathcal{M} = \mathcal{M}_0^n$. Over $K'$, the sections $t_j$ are written in terms of a very ample family $s_0, \ldots, s_N$ of $\mathcal{H}$, with uniquely determined coefficients $g_{jk}$, which gives 1. For $\sigma \in D$, twisting the section $t_j$ by $\varphi_\sigma$ gives a section of $\mathcal{M}$ over $G$. It is therefore a $W$-combination $\sum_l c_l t_l$ of the basis. Comparing coefficients over $K'$ gives $\sigma(g_{jk}) = \sum_l c_l g_{lk}$, which is 2 with $h_\sigma = (c_l)$. $\square$

**Lemma 3.2.7 (Matrix descent).** In an unramified descent setting, let $g \in M_n(K')$ have invertible determinant, and assume that for each $\sigma \in D$ there is $h_\sigma \in M_n(W)$ with $\sigma(g) = h_\sigma g$. Then there are $h \in M_n(W)$ with $\det h \in W^\times$ and $k \in M_n(K)$ with $k = h g$ in $M_n(K')$.

Lean: `GlobalTheory.T.matrix_descent_unramified_dvr`.

*Proof.* The rows of $g$ span a lattice $\Lambda = W^n g$ in $K'^n$. The hypothesis says $\sigma(\Lambda) \subseteq \Lambda$ for $\sigma \in D$. Since $R \to W$ is unramified and the residue condition holds, such a lattice is spanned over $W$ by vectors in $K^n$, that is, by an $R$-lattice of $K^n$. A basis of it gives the rows of $k$, and $h$ is the change of basis matrix of $\Lambda$. $\square$

### The two theorems

**Theorem 3.2.8 (Compatible projective embeddings).** In an unramified descent setting with a descent datum on $G$, there are a quasi-separated scheme $P$ over $R$ and morphisms $i_A : A \to P$ and $i_G : G \to P$ over $R$ such that the following hold.

1. The induced morphism $A \to P \times_R K$ is a closed immersion.
2. The induced morphism $G \to P \times_R W$ is a closed immersion.
3. On $G \times_W K'$, $i_A \circ \mathrm{pr}_A \circ e = i_G \circ \mathrm{pr}_G$, where $\mathrm{pr}_A : A \times_K K' \to A$ and $\mathrm{pr}_G : G \times_W K' \to G$ are the projections.

Lean: `UpperTheory.Lit.Nos.C3.exists_compatible_projective_embeddings`.

*Proof.* Take $N$, $\mathcal{H}$, $s$, $\mathcal{M}$, $t$, $w$ and $g$ from the lemma on a stable matrix. By matrix descent there are $h \in M_{N+1}(W)$ with unit determinant and $k \in M_{N+1}(K)$ with $k = hg$. The image of $\det k$ in $K'$ is $\det h \cdot \det g$, a unit, so $\det k \neq 0$ and $\det k \in K^\times$.

Put $s'_j = \sum_m k_{jm} s_m$ and $t'_j = \sum_l h_{jl} t_l$. By the lemma on linear change, both families are very ample, over $K$ and over $W$. On $G \times_W K'$, through $w$ and $e$,
$$
\begin{aligned}
t'_j &= \sum_l h_{jl} t_l = \sum_l h_{jl} \sum_m g_{lm} s_m \\
&= \sum_m (hg)_{jm} s_m = \sum_m k_{jm} s_m = s'_j .
\end{aligned}
$$

Let $P = \mathbb{P}^N_R$, which is separated, hence quasi-separated. Let $i_A$ be the morphism $A \to \mathbb{P}^N_K$ given by $(s'_j)$, followed by the projection $\mathbb{P}^N_K \to \mathbb{P}^N_R$. Let $i_G$ be the morphism $G \to \mathbb{P}^N_W$ given by $(t'_j)$, followed by $\mathbb{P}^N_W \to \mathbb{P}^N_R$. Both are closed immersions into the base changes of $P$, as $A$ and $G$ are proper, hence separated. The two composites in 3 are the morphisms $G \times_W K' \to \mathbb{P}^N_R$ given by the pulled back families $(t'_j)$ and $(s'_j)$, which agree by the display. $\square$

**Theorem 3.2.9 (Descent of the model).** In an unramified descent setting, there are a scheme $X$ over $R$ and morphisms $a : A \to X$ and $g : G \to X$ such that the following hold.

1. The square formed by $a$ is cartesian: $A = X \times_R K$.
2. The square formed by $g$ is cartesian: $G = X \times_R W$.
3. On $G \times_W K'$, $a \circ \mathrm{pr}_A \circ e = g \circ \mathrm{pr}_G$.

Lean: `UpperTheory.Lit.Nos.C4.exists_scheme_model_descent_unramified`.

*Proof.* By the lemma on the existence of the descent datum, $G$ carries a descent datum. By the theorem on compatible projective embeddings there are $P$, $i_A$ and $i_G$ as there. Let $X$ be the scheme theoretic closure of $i_A(A)$ in $P$. Since $A$ is closed in $P \times_R K$, $X \times_R K = A$. The map $R \to W$ is flat, as $W$ is torsion free over the discrete valuation ring $R$, and the formation of the scheme theoretic closure commutes with flat base change. So $X \times_R W$ is the closure in $P \times_R W$ of the image of $A \times_K K'$, which by 3 of the previous theorem is the image of $G \times_W K'$. Since $G$ is flat over $W$ and closed in $P \times_R W$, it is the closure of its generic fibre, so $X \times_R W = G$. The compatibility 3 follows from that of $i_A$ and $i_G$. $\square$

**Remark 3.2.10 (Formalization).** The last step of the descent of the model, from the embeddings to $X$, is `GlobalTheory.T.abelian_variety_extends_unramified`, which is cited and not unfolded; the closure argument above is the classical one. The descent datum is `GlobalTheory.T.galois_descent_integral_structure`, and it uses only $\sigma(W) \subseteq W$, not the condition on $\sigma^{-1}$. The lemma on a stable matrix rests on further results which we have not unfolded: the extension of line bundles from the generic fibre, the very ample family of a power, and the extension of twisted sections, `UpperTheory.Lit.Nos.C1.twisted_sections_extend`. In both theorems $D$ is any set of automorphisms; no group structure is asked. The conclusion of the descent of the model does not say that $X$ is an abelian scheme over $R$: this is the next step, in [the next section](/entry/has-good-reduction-of-inertia-fixed/). The helper lemmas on sections of [ExistsCompatibleProjectiveEmbeddings.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/GoodReduction/ExistsCompatibleProjectiveEmbeddings.lean#L21) compute pullbacks of constant sections and of linear combinations; they are used in the display above.
