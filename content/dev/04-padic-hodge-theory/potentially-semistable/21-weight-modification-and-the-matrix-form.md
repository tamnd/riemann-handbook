---
title: Weight modification and the matrix form
decls:
  - GlobalTheory.T.monodromy_irreducible_elementary_weightModification
  - GlobalTheory.PMon.modStep_holds
  - GlobalTheory.T.pAdicMonodromyTheorem_matrixForm
  - GlobalTheory.PMon.matThm_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Weight modification and the matrix form

This section proves the matrix form of the monodromy theorem, which [the $p$-adic monodromy theorem](/entry/de-rham-potentially-semistable/) was reduced to. A de Rham admissible representation carries integer weights, one for each level $m < r$ and each basis index $j$. After a twist the weights add up to zero. The proof then lowers the sum of the squares of the weights, one elementary step at a time, until all weights vanish, and the case of weight zero is Sen's theorem. A step is possible when the representation does not split. When it splits, we induct on the dimension. The elementary step is the weight modification, and it rests on [the lattice lemma](/entry/fundamental-lemma-lattice-frob-fixed-forall-degree/).

We keep the notation of [the previous section](/entry/fundamental-lemma-lattice-frob-fixed-forall-degree/) and of the matrix form: $\rho : G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$, $r$-rational, de Rham admissible and semistable admissible representations, the cyclotomic character $\chi$, $\mathrm{GL}_n(\mathrm{Fil}^0)$, and the exponents $\varepsilon_{x,y}$. For $m \geq 0$ and $g \in G_K$ write $\rho_m(g)$ for the matrix $\sigma^m(\rho(g))$, with its entries mapped into $B_{\mathrm{dR}}$.

**Definition 6.21.1 (Framed and split representations).** Let $r \geq 0$ and $\rho : G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$.

1. Let $w : \{0, \dots, r-1\} \times n \to \mathbb{Z}$. Then $\rho$ is *framed with weights $w$* if for every $m < r$ there is $U_m \in \mathrm{GL}_n(\mathrm{Fil}^0)$ with
$$\rho_m(g)\, g(U_m) = U_m \cdot \operatorname{diag}\big(\chi(g)^{w(m,j)}\big)_{j \in n} \quad \text{for all } g \in G_K.$$
2. $\rho$ *splits at level $r$* if there are a subset $s \subseteq n$, nonempty and not all of $n$, and $p \in \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ whose entries are fixed by $\sigma^r$, such that $(p^{-1}\rho(g)\,p)_{ij} = 0$ for all $g \in G_K$, $i \notin s$ and $j \in s$.

Lean: `GlobalTheory.PMon.Framed` (also `GlobalTheory.PMon.Splits`, the second condition).

The columns of $U_m$ are eigenvectors of the twisted action $v \mapsto \rho_m(g)\, g(v)$ with eigencharacters $\chi^{w(m,j)}$. If $\rho$ splits, then after the change of basis $p$ the span of the basis vectors in $s$ is stable, so $\rho$ is reducible over the field of $\sigma^r$-fixed elements.

**Definition 6.21.2 (The five steps).** Each of the following statements quantifies over every prime $\ell$, all tied local period data, every finite set $n$, every finite extension $K$ of $\mathbb{Q}_\ell$, every $r \geq 0$ and every $\rho : G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ that is $r$-rational.

1. (Frames.) $\rho$ is de Rham admissible if and only if it is framed with some weights $w$.
2. (Twist.) If $\rho$ is framed with weights $w$, there are a finite extension $K'$ of $\mathbb{Q}_\ell$, an integer $r' \geq 0$, an $r'$-rational $\rho' : G_{K'} \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ and weights $w'$ with $\rho'$ framed with weights $w'$, $\sum_{m,j} w'(m,j) = 0$, and such that $\rho$ is semistable admissible if $\rho'$ is.
3. (Sen.) If $\rho$ is framed with weights $0$, then $\rho$ is semistable admissible.
4. (Reduction.) Assume that $\rho$ is de Rham admissible and splits at level $r$, and that every $r$-rational, de Rham admissible $\rho' : G_K \to \mathrm{GL}_a(\mathbb{Q}_\ell^{\mathrm{ur}})$ with $|a| < |n|$ is semistable admissible. Then $\rho$ is semistable admissible.
5. (Modification.) Let $\rho$ be framed with weights $w$, not split at level $r$, and let $x \neq y$ in $\{0, \dots, r-1\} \times n$. Then there is an $r$-rational $\rho' : G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$, framed with weights $w + \varepsilon_{x,y}$, such that $\rho$ is semistable admissible if $\rho'$ is.

Lean: `GlobalTheory.PMon.FrameEx` (also `GlobalTheory.PMon.TwistStep`, `GlobalTheory.PMon.SenStep`, `GlobalTheory.PMon.RedStep` and `GlobalTheory.PMon.ModStep`, steps 2 to 5).

The weight modification raises the weight at $y$ by one and lowers the weight at $x$ by one. Steps 1 and 2 are proved elsewhere in this development. Step 3 is [the weight zero case](/entry/weight-zero-potentially-semistable-of-sen-theorem/), and step 4 is [the reduction for split representations](/entry/potentially-semistable-reducible-unramified-split/). We prove step 5 here, from the following facts, proved elsewhere in this development. In both, $\rho$ is $r$-rational.

1. (Independence of an eigenvector.) Let $\rho$ not split at level $r$, let $m \geq 0$ and $a \in \mathbb{Z}$, and let $u \in (\mathrm{Fil}^0)^n$ with some $u_i \notin \mathrm{Fil}^1$ and $\rho_m(g)\, g(u) = \chi(g)^a u$ for all $g \in G_K$. Then for every $c \in (\mathbb{Q}_\ell^{\mathrm{ur}})^n$ with $\sigma^r(c_i) = c_i$ for all $i$, $\sum_i c_i u_i \in \mathrm{Fil}^1$ implies $c = 0$.
2. (Change of frame.) Let $w, e : \{0, \dots, r-1\} \times n \to \mathbb{Z}$, let $U_0, \dots, U_{r-1} \in \mathrm{GL}_n(B_{\mathrm{dR}})$ with $\rho_m(g)\, g(U_m) = U_m \operatorname{diag}(\chi(g)^{w(m,j)})$ for all $m$ and $g$, and let $A \in \mathrm{GL}_n(B)$ with entries fixed by $\varphi^r$, such that for every $m < r$ there is $W_m \in \mathrm{GL}_n(\mathrm{Fil}^0)$ with $\iota_m(A) = U_m \operatorname{diag}(t^{e(m,j)})\, W_m$. Then there is an $r$-rational $\rho' : G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$, framed with weights $w + e$, such that $\rho$ is semistable admissible if $\rho'$ is.

In fact 1, the vector $u$ spans a line over $B_{\mathrm{dR}}$ that is stable under the twisted action. A relation modulo $\mathrm{Fil}^1$ with $\sigma^r$-fixed coefficients would give a proper subrepresentation defined over that field, and so a splitting. In fact 2, the new representation is the action on the lattice spanned by the columns of $A$.

**Theorem 6.21.3 (Weight modification).** Step 5 holds: let $\rho : G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$ be $r$-rational, framed with weights $w$ and not split at level $r$, and let $x \neq y$ in $\{0, \dots, r-1\} \times n$. Then there is an $r$-rational $\rho'$, framed with weights $w + \varepsilon_{x,y}$, such that $\rho$ is semistable admissible if $\rho'$ is.

Lean: `GlobalTheory.T.monodromy_irreducible_elementary_weightModification` (also `GlobalTheory.PMon.modStep_holds`, a second name).

*Proof.* Choose $U_0, \dots, U_{r-1} \in \mathrm{GL}_n(\mathrm{Fil}^0)$ as in the definition of a framed representation. Write $x = (x_1, x_2)$ and let $u$ be the column $x_2$ of $U_{x_1}$, so $u_i = (U_{x_1})_{i, x_2}$.

Step 1: $u$ is not in $\mathrm{Fil}^1$. The element $1$ is not in $\mathrm{Fil}^1$. The entry $(x_2, x_2)$ of $U_{x_1}^{-1} U_{x_1} = 1$ gives
$$1 = \sum_{k} (U_{x_1}^{-1})_{x_2, k}\, u_k.$$
The entries of $U_{x_1}^{-1}$ lie in $\mathrm{Fil}^0$. If every $u_k$ were in $\mathrm{Fil}^1$, then every term would be in $\mathrm{Fil}^0 \cdot \mathrm{Fil}^1 \subseteq \mathrm{Fil}^1$, and so would $1$. Hence some $u_k \notin \mathrm{Fil}^1$. All $u_k$ lie in $\mathrm{Fil}^0$, since $U_{x_1}$ has entries in $\mathrm{Fil}^0$.

Step 2: $u$ is an eigenvector. Take the column $x_2$ of the frame equation at level $x_1$. Since the diagonal matrix multiplies column $x_2$ by $\chi(g)^{w(x)}$,
$$\rho_{x_1}(g)\, g(u) = \chi(g)^{w(x)}\, u \quad \text{for all } g \in G_K.$$

Step 3: independence. By fact 1, applied with $m = x_1$ and $a = w(x)$, every $c \in (\mathbb{Q}_\ell^{\mathrm{ur}})^n$ with $\sigma^r$-fixed entries and $\sum_i c_i (U_{x_1})_{i, x_2} \in \mathrm{Fil}^1$ is zero. This is the hypothesis of the lattice lemma in degree $r$ for $U$ and the index $x$.

Step 4: the lattice. Since $x \neq y$ and all $U_m \in \mathrm{GL}_n(\mathrm{Fil}^0)$, [the lattice lemma](/entry/fundamental-lemma-lattice-frob-fixed-forall-degree/) gives $A \in \mathrm{GL}_n(B)$ with entries fixed by $\varphi^r$, and for every $m < r$ some $W_m \in \mathrm{GL}_n(\mathrm{Fil}^0)$ with
$$\iota_m(A) = U_m \cdot \operatorname{diag}\big(t^{\varepsilon_{x,y}(m,j)}\big) \cdot W_m.$$

Step 5: the new representation. Fact 2, with $e = \varepsilon_{x,y}$, gives $\rho'$. $\square$

The weights are changed by $\varepsilon_{x,y}$, whose entries sum to zero. To choose $x$ and $y$ we use the following lemma.

**Lemma 6.21.4 (Lowering the sum of squares).** Let $Z$ be a finite set and $f : Z \to \mathbb{Z}$ with $\sum_z f(z) = 0$ and $f \neq 0$. Then there are $x \neq y$ in $Z$ with
$$\sum_z \big(f(z) + \varepsilon_{x,y}(z)\big) = 0, \qquad \sum_z \big(f(z) + \varepsilon_{x,y}(z)\big)^2 < \sum_z f(z)^2.$$

Lean: `GlobalTheory.PMon.arith`.

*Proof.* If $f(z) \leq 0$ for all $z$, then a sum of nonpositive integers is zero, so $f = 0$. Hence there is $x$ with $f(x) > 0$. In the same way there is $y$ with $f(y) < 0$, and $x \neq y$. For every $g : Z \to \mathbb{Z}$ we have $\sum_z g(z)\, \varepsilon_{x,y}(z) = g(y) - g(x)$. With $g = 1$ this gives the first claim. For the second,
$$\begin{aligned} \sum_z \big(f(z) + \varepsilon_{x,y}(z)\big)^2 &= \sum_z f(z)^2 + 2\big(f(y) - f(x)\big) + \big(\varepsilon_{x,y}(y) - \varepsilon_{x,y}(x)\big) \\ &= \sum_z f(z)^2 + 2\big(f(y) - f(x)\big) + 2. \end{aligned}$$
Since $f(y) \leq -1$ and $f(x) \geq 1$, we get $2(f(y) - f(x)) + 2 \leq -2 < 0$. $\square$

**Theorem 6.21.5 (Reduction to the five steps).** If steps 1 to 5 hold, then the matrix form of the monodromy theorem holds.

Lean: `GlobalTheory.PMon.matThm_of_steps` (also `GlobalTheory.T.padicMonodromyMatrixForm_of_induction_cases`, a second name).

*Proof.* Fix $\ell$ and the period data. We prove, by strong induction on $N$, that for every $n$ with $|n| = N$, every $K$ and $r$, and every $r$-rational, de Rham admissible $\rho : G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$, the representation $\rho$ is semistable admissible. Assume this for all sizes below $N$, and let $|n| = N$ and $\rho$ be given.

By step 1, $\rho$ is framed with some weights $w$. Step 2 gives $K'$, $r'$, an $r'$-rational $\rho'$ on $G_{K'}$ and weights $w'$ with $\sum w' = 0$, and it is enough to show that $\rho'$ is semistable admissible. We prove, by strong induction on $S \geq 0$, the following claim: every $r'$-rational $\tau : G_{K'} \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$, framed with weights $v$ such that $\sum_z v(z) = 0$ and $\sum_z v(z)^2 = S$, is semistable admissible. The claim for $\tau = \rho'$ and $v = w'$ finishes the proof.

Let $\tau$ and $v$ be as in the claim, and assume the claim for all values below $S$. There are three cases.

1. If $v = 0$, then $\tau$ is semistable admissible by step 3.
2. If $\tau$ splits at level $r'$, then $\tau$ is de Rham admissible by step 1, since it is framed with weights $v$. Every $r'$-rational, de Rham admissible representation of $G_{K'}$ of size less than $|n| = N$ is semistable admissible by the outer induction. So $\tau$ is semistable admissible by step 4.
3. Otherwise $v \neq 0$ and $\tau$ does not split. The lemma on lowering the sum of squares, with $Z = \{0, \dots, r'-1\} \times n$ and $f = v$, gives $x \neq y$ with $\sum_z (v + \varepsilon_{x,y})(z) = 0$ and $\sum_z (v + \varepsilon_{x,y})(z)^2 < S$. Step 5 gives an $r'$-rational $\tau'$, framed with weights $v + \varepsilon_{x,y}$, such that $\tau$ is semistable admissible if $\tau'$ is. The inner induction applies to $\tau'$, so $\tau'$ is semistable admissible, and then so is $\tau$. $\square$

**Theorem 6.21.6 (Matrix form of the monodromy theorem).** For every prime $\ell$, all tied local period data, every finite set $n$, every finite extension $K$ of $\mathbb{Q}_\ell$, every $r \geq 0$ and every $\rho : G_K \to \mathrm{GL}_n(\mathbb{Q}_\ell^{\mathrm{ur}})$, if $\rho$ is $r$-rational and de Rham admissible, then $\rho$ is semistable admissible.

Lean: `GlobalTheory.T.pAdicMonodromyTheorem_matrixForm` (also `GlobalTheory.PMon.matThm_holds`, a second name).

*Proof.* Steps 1 and 2 hold, as proved elsewhere in this development. Step 3 holds by [the weight zero case](/entry/weight-zero-potentially-semistable-of-sen-theorem/), step 4 by [the reduction for split representations](/entry/potentially-semistable-reducible-unramified-split/), and step 5 by the [theorem on weight modification](/entry/monodromy-irreducible-elementary-weight-modification/). The theorem on the reduction to the five steps gives the claim. $\square$

This is the matrix form that [the $p$-adic monodromy theorem](/entry/de-rham-potentially-semistable/) uses.

**Remark 6.21.7 (Formalization).** The proof of `GlobalTheory.PMon.matThm_holds` is one term ([PAdicMonodromyTheoremMatrixForm.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/PAdicMonodromyTheoremMatrixForm.lean#L14)) that applies `GlobalTheory.T.padicMonodromyMatrixForm_of_induction_cases` to five names under `GlobalTheory.T`. These, like the two names of each theorem here, are `first | exact ...` wrappers under `maxHeartbeats 1000000`. Steps 1 and 2 are `GlobalTheory.T.deRham_iff_framed_galois_representation` and `GlobalTheory.T.lubinTateTwistTotalWeightZero_proof`, wrappers of `GlobalTheory.PMon.FrameEquiv.frameEx` and `GlobalTheory.PMon.twistStep`; neither is in the outline of this chapter. Facts 1 and 2 are `GlobalTheory.T.residue_indep_of_not_reducibleOverUnramified` and `GlobalTheory.T.exists_rep_of_frobeniusFixed_frame_change`. In the proof of the weight modification ([MonodromyIrreducibleElementaryWeightModification.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/MonodromyIrreducibleElementaryWeightModification.lean#L52)), the hypothesis $x \neq y$ is passed to the lattice lemma and used nowhere else, and only the frame at level $x_1$ enters fact 1. The inner induction in [PadicMonodromyMatrixFormOfInductionCases.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/PadicMonodromyMatrixFormOfInductionCases.lean#L57) runs on the natural number `(∑ z, v z.1 z.2 ^ 2).toNat`, and the bound uses that this sum is nonnegative (line 73).
