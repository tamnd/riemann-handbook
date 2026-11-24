---
title: Weights of frame classes over one datum
decls:
  - GlobalTheory.DegAsm.PerDat.one_class
  - GlobalTheory.DegAsm.sum_weights_per_datum
  - GlobalTheory.TypeAsm.PerRow.sum_clsOm_le_datBd
  - GlobalTheory.T.sum_frameClassWeights_le_datumBound
  - GlobalTheory.TypeAsm.PerRow.sum_classes_le
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Weights of frame classes over one datum

In this section the lattice $\Lambda$ and the first flag $F$ are fixed, and the second flag varies. Two second flags are in the same frame class if a unipotent map of $F$ that fixes $\Lambda$ moves one to the other, up to the flag. We bound the sum of the weights of the frame classes with a given embedded datum by an explicit datum bound. The weight of a second flag is the least weight over all normal forms adapted to the pair. The result feeds the per row count of term pairs in the next section, and so the pair count of the [type bound](/entry/rows-pos-type-p/).

We keep the notation of [the weight of a split term](/entry/om-le/) and of [the orbit sums](/entry/om-sum-same-dat-le/). Let $K$ be an unramified CM field, let $(V, H)$ be a Hermitian space and let $F$ be a flag datum of length $r$.

### Adapted normal forms and the embedded datum

**Definition 2.3.1 (Adapted normal form).** Let $G$ be a second flag datum and $\mathfrak{d}$ a nonzero ideal. A normal form $N$ is *adapted* to $(F, G, \mathfrak{d})$ if its ideal is $\mathfrak{d}$, its first flag has the same graded pieces as $F$, and its second flag has the same graded pieces as $G$.

**Definition 2.3.2 (Weight of a second flag).** For a lattice $\Lambda$ let $\omega_{\inf}(F, G, \mathfrak{d}, \Lambda)$ be the infimum of the weights $\omega_N(\Lambda)$ over the normal forms $N$ adapted to $(F, G, \mathfrak{d})$.

**Definition 2.3.3 (Embedding along a flag).** Let $(W, H_W)$ be a Hermitian space. A linear map $\epsilon \colon W \to V$ is an *embedding along $F$* if $H(\epsilon x, \epsilon y) = H_W(x, y)$ for all $x, y$, and if a vector $v \in V$ is orthogonal to $e_0, \dots, e_r$ exactly when $v \in \epsilon(W) + X$.

**Definition 2.3.4 (Embedded datum).** For an embedding $\epsilon$ along $F$, a second flag $G$, a level $g$ and a lattice $\Lambda$, the *embedded datum* $d(F, G, \epsilon, g, \Lambda)$ is the pair of the preimage under $\epsilon$ of the definite part of $\Lambda$ for $(G, F)$ plus $X$, and the preimage under $\epsilon \times \epsilon$ of the gluing graph of $\Lambda$ modulo $g$ plus $X \times X$.

**Definition 2.3.5 (Frame equivalence).** Two second flags $G$ and $G'$ are *frame equivalent* for $(F, \Lambda)$ if there is a map $n$ that is unipotent for $F$, with $n\Lambda = \Lambda$ and $n(G.e_a) - G'.e_a \in G'.X_a$ for each $a \le r$.

**Definition 2.3.6 (Datum bound).** For $k, r \in \mathbb{N}$ and real numbers $\Delta, D_b, N_T, x$ put
$$\begin{aligned}
B(k, r, \Delta, D_b, N_T, x) = {}& \Big(\frac{\Delta}{x}\Big)^{k/2} 8^{r+1} f^2\, \Delta^{3 c_f + 6} \\
&\cdot N_T^2\, (D_b\, \Delta\, N_T)^{10000(r+1)^3}.
\end{aligned}$$

### One class of normal forms

**Lemma 2.3.7 (Normal forms with the same invariants).** Let $(W, H_W)$ be a Hermitian space with an embedding $\epsilon$ along $F$, let $g \ge 1$, let $\Lambda$ be a lattice and let $\mathfrak{d}$ be a nonzero ideal. Let $N_0$ be a normal form adapted to $(F, G_0, \mathfrak{d})$ for which $\Lambda$ is a term of level $g$. Let $(G_i)_{i \in s}$ be a finite family of second flags with normal forms $N_i$ such that for each $i \in s$:

1. $N_i$ is adapted to $(F, G_i, \mathfrak{d})$ and $\Lambda$ is a term of level $g$ for $N_i$;
2. $N_i$ and $N_0$ have the same index $j$, the same scalar $c$ and the same $T$;
3. the pairing matrices of $N_i$ and $N_0$ in the first $j$ rows and columns are equal;
4. $d(F, G_i, \epsilon, g, \Lambda) = d(F, G_0, \epsilon, g, \Lambda)$;

and such that $G_i$ and $G_{i'}$ frame equivalent implies $i = i'$. Then, with the invariants of $N_0$,
$$\sum_{i \in s} \omega_{\inf}(F, G_i, \mathfrak{d}, \Lambda) \le N_T^2 \Big(\frac{\Delta}{g_I(\Lambda)}\Big)^{\dim W/2} \Delta^{c_f+2} (D_b \Delta N_T)^{10000(r+1)^3}.$$

Lean: `GlobalTheory.DegAsm.PerDat.one_class`.

*Proof.* Normal forms with the same $j$, $c$, $T$ and pairing matrix are unique up to a unipotent map. So for each $i$ there is $\sigma_i$, unipotent for both flags of $N_0$, that carries $N_0$ to a normal form adapted to $(F, G_i, \mathfrak{d})$. Moving $N_0$ by $\sigma_i$ moves its weights: $\omega_{\inf}(F, G_i, \mathfrak{d}, \Lambda) \le \omega_{N_0}(\sigma_i^{-1}\Lambda)$.

The lattices $\sigma_i^{-1}\Lambda$ are terms for $N_0$. The embedded datum does not change under unipotent maps, so by condition 4 they satisfy the three conditions of [the corollary on inequivalent terms](/entry/fixed-form-main/). If $\rho \sigma_i^{-1}\Lambda = \sigma_{i'}^{-1}\Lambda$ with $\rho \in R$, then $\sigma_{i'} \rho \sigma_i^{-1}$ fixes $\Lambda$ and moves $G_i$ to $G_{i'}$ up to the flag, so $i = i'$. The invariants of an adapted normal form give $\dim \widetilde W = \dim W$. The corollary then gives the bound. $\square$

### One datum

**Theorem 2.3.8 (Weights of the second flags of one datum).** Let $(W, H_W)$ be a Hermitian space with an embedding $\epsilon$ along $F$. Let $\mathfrak{d}$ be a nonzero ideal, let $g, j, T, x \in \mathbb{N}$ with $g \ge 1$ and $x \ge 1$, let $\delta \colon \mathbb{N} \to K$, let $\Lambda$ be a lattice, let $d$ be a datum and let $\Delta \ge 1$ and $D_b \ge 1$. Let $(G_i)_{i \in s}$ be a finite family of second flags such that for each $i \in s$:

1. there is a normal form $N$ adapted to $(F, G_i, \mathfrak{d})$ for which $\Lambda$ is a term of level $g$, with index $j$, with $T$, with $\Delta_N = \Delta$, with $D_{b,N} = D_b$ and with $g_I(\Lambda) = x$;
2. the leading minors $D_l$ of the pair $(F, G_i)$ for $l \le j$ are the values $\delta(l)$;
3. $d(F, G_i, \epsilon, g, \Lambda) = d$;

and such that $G_i$ and $G_{i'}$ frame equivalent implies $i = i'$. Then
$$\sum_{i \in s} \omega_{\inf}(F, G_i, \mathfrak{d}, \Lambda) \le B(\dim W, r, \Delta, D_b, T^f, x).$$

Lean: `GlobalTheory.DegAsm.sum_weights_per_datum`.

*Proof.* Sort the family by two invariants of the normal forms: the pairing matrix in the first $j$ rows and columns, and the scalar $c$. The pairing matrix is a signed block antidiagonal matrix with the leading minors $\delta(1), \dots, \delta(j)$, and there are at most $8^j$ of these. The scalar $c$ is a norm one element that is a quotient of ideals with norm bounded in terms of $\Delta$, and there are at most $8 f^2 \Delta^{2(2+c_f)}$ of these.

On each fibre the lemma above applies with $N_0$ any normal form of the fibre, and it gives the bound $N_T^2 (\Delta/x)^{\dim W/2} \Delta^{c_f+2} (D_b \Delta N_T)^{10000(r+1)^3}$. Sum over the fibres. Since $j \le r$, the product $8^j \cdot 8 f^2 \Delta^{4 + 2c_f} \cdot \Delta^{c_f + 2}$ is at most $8^{r+1} f^2 \Delta^{3c_f + 6}$. $\square$

### Frame classes of terms

Now the first flag comes from the term setting of the type bound. In that setting there is a CM field $E$ with the ranks $k$, $r$ and $f$, a family of terms $t$ for a word $u$, each with a lattice $\Lambda_t$ and a second flag $F_t$, and the first flag $F_0$ of the word. The set of relevant terms is fixed by the setting. Each term has an index $j(t) = r - \dim I_t$ and labels $\delta_t(l)$, which are the leading minors for $l \le j(t)$ and $0$ after. Its weight is $\omega(t) = \omega_{\inf}(F_0, F_t, \mathfrak{d}_I, \Lambda_t)$ for an ideal $\mathfrak{d}_I$ fixed by the setting. The numbers $\Delta(j, \delta)$ and $D_b(j, \delta)$ are the local norms of the labels, and $N_T(u) = T_u^f$.

For a lattice $\Lambda$, the *frame class* of a term $t$ with $\Lambda_t = \Lambda$ is the frame equivalence class of $F_t$ for $(F_0, \Lambda)$. The *class weight* of a class is the weight of a chosen term in it, and $0$ if there is none.

**Theorem 2.3.9 (Weights of frame classes).** Assume the standing hypotheses of the setting. Let $(W, H_W)$ be a Hermitian subspace with the inclusion an embedding along $F_0$. Let $\Lambda$ be a lattice, let $j, x \in \mathbb{N}$, let $\delta$ be a label and let $d$ be a datum. Let $A$ be a nonempty finite set of terms such that each $t \in A$ is relevant, has $\Lambda_t = \Lambda$, $j(t) = j$ and $\delta_t = \delta$, has an adapted normal form $N_t$ for which $\Lambda$ is a term of level $g$ with $g_I(\Lambda) = x$, and has embedded datum $d$. Here $g$ is the level of the setting. Then the sum of the class weights over the frame classes of the terms in $A$ is at most
$$B\big(k, r, \Delta(j, \delta), D_b(j, \delta), N_T(u), x\big).$$

Lean: `GlobalTheory.TypeAsm.PerRow.sum_clsOm_le_datBd` (also `GlobalTheory.T.sum_frameClassWeights_le_datumBound` and `GlobalTheory.TypeAsm.PerRow.sum_classes_le`, second names).

*Proof.* Two terms of $A$ have the same frame class exactly when their second flags are frame equivalent. Pick one term in each class; the class weight is its weight. The chosen terms satisfy the hypotheses of the previous theorem, with $\dim W = k$ and with $\Delta$, $D_b$ and $T$ from the setting. Their second flags are pairwise not frame equivalent. The previous theorem gives the bound. $\square$

**Remark 2.3.10 (Formalization).** Adapted normal forms are `GlobalTheory.DegAsm.Adapt` and the weight of a second flag is `omI`, an `sInf` over a set of reals; if no normal form is adapted it is the infimum of the empty set. The embedding is `IsEmb`, the datum `datOf`, frame equivalence `FrEqv` and the datum bound `datBd`, all in AdaptSelf.lean. The lemma and the theorem are in FlagFrameVectorMemCommonSubspace.lean (lines 120 and 204); that file is named after a small lemma near its top. The name `one_class` is misleading: the lemma sums over a whole family of classes. Its proof uses `hermFramePairNormalForm_unique_up_to_unipotent`, `exists_hermFramePairNormalForm_moved_by_isometry`, `WeightInf.main`, `adapt_invariants`, `finrank_wt` and `embeddedDatum_invariant_under_unipotent`. The proof of the theorem uses `signedBlockAntidiag_with_leadingMinors_encard_le`, `hermFramePair_scalar_eq_quot_ideals_norm_le`, `NormOneCount.main` and `sum_le_of_fibres`; the hypothesis `hx` is not used by name. The frame class is `frCls` and the class weight `clsOm`, which uses `Classical.choose` and is $0$ off the image; `frCls_eq_iff` is in ClsOmNonneg.lean, line 16. `sum_classes_le` (TermPairsRowLatticeCountedViaEmbeddings.lean, line 49) restates the theorem word for word and is proved by a direct call, so it is a third name. The setting objects `D7`, `HidaSetting`, `Full`, `Std`, `relSet`, `jT`, `labT`, `k2Del`, `DbL` and `dI` are not unfolded here. The statement file SumFrameClassWeightsLeDatumBoundStatement.lean imports `Mathlib` twice.
