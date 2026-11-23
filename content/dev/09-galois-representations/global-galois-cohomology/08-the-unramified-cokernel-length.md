---
title: The unramified cokernel length
decls:
  - ReciprocityTheory.PGsh.Up.unramifiedCokernelLength_of_frobeniusLengthBound
  - ReciprocityTheory.PGsh.Up.frobenius_of_group
  - ReciprocityTheory.PGsh.Up.u7
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The unramified cokernel length

This section proves a length formula in $p$-adic linear algebra. The input is a lattice of rank $2g$ over $\mathbb{Z}_p$ with an alternating pairing, an action of a ring $O$, a Hodge-Tate map and a Hopf order. The model case is the Tate module of an abelian variety with good reduction and multiplication by $O$, over a [[local field|J85FZEQG38]]. The output compares the lengths of two cokernels of the Hodge-Tate map between conjugate eigenspaces. The difference of the two lengths is an explicit number that depends only on the ranks of the eigenspaces and on how Frobenius permutes the embeddings of $O$. The result feeds [the bound for unramified linear data](/entry/lin-dat-unram-bound/) in Volume 4. Background is in [admissible and Hodge-Tate representations](/learn/padic-hodge/#admissible-representations-and-hodge-tate-representations) and in [the cyclotomic character and Tate modules](/learn/galois-representations/#the-cyclotomic-character-and-tate-modules).

### Hodge-Tate data

Fix a prime $p \neq 2$ and an integer $g \geq 0$. Let $C$ be an algebraically closed field of characteristic $0$ with a valuation $v : C \to \mathbb{R}_{\geq 0}$, written multiplicatively, and let $R$ be its ring of integers. Assume $0 < v(p) < 1$. Let $O$ be a $\mathbb{Z}_p$-algebra with an involution $\sigma$, and let $c_p \in R$ with $v(c_p)^{p-1} = v(p)$.

Let $T = \mathbb{Z}_p^{2g}$. A *Hodge-Tate datum* consists of the following.

1. A $\mathbb{Z}_p$-algebra map $\rho : O \to \operatorname{End}(T)$ and a ring map $\rho_L : O \to M_g(R)$.
2. An alternating matrix $E$ on $T$ with unit determinant such that $\rho(a)^{\mathsf T} E = E\, \rho(\sigma a)$ for all $a \in O$.
3. Two $g \times 2g$ matrices $H_t$ and $B_t$ over $R$ with $H_t \rho(a) = \rho_L(\sigma a)^{\mathsf T} H_t$ and
$$B_t^{\mathsf T} H_t - H_t^{\mathsf T} B_t = c_p E.$$
4. A Hopf order $A$ of functions on $N = (\mathbb{Z}/p)^{2g}$ with values in $C$, stable under $\rho$, such that each row of $H_t$ and of $B_t$ is congruent modulo $p$ to a function in $A$.
5. A surjective $R$-linear map from the augmentation ideal $I$ of $A$ onto $(R/p)^g$, with kernel $I^2$, that is linear for $\rho_L$.

In the model case $E$ is the Weil pairing, $\sigma$ is the Rosati involution, $H_t$ is the Hodge-Tate map, $A$ is the coordinate ring of the $p$-torsion group scheme, and item 5 says that the cotangent space of the $p$-torsion is $\omega / p\omega$.

### Unramified eigen data

An *unramified eigen datum* for a Hodge-Tate datum is a finite index set $\{1, \dots, m\}$ with the following.

1. Ring maps $s_i : O \to R$, which play the part of embeddings.
2. Orthogonal idempotents $\varepsilon^T_i$ on $R^{2g}$ and $\varepsilon^L_i$ on $R^g$ with sum $1$, such that $\rho(a) \varepsilon^T_i = s_i(a) \varepsilon^T_i$ and $\rho_L(a)\varepsilon^L_i = s_i(a) \varepsilon^L_i$.
3. A permutation $c$ (conjugation) with $s_{c(i)}(a) = s_i(\sigma a)$, and a permutation $\varphi$ (Frobenius) with $v(s_{\varphi(i)}(a) - s_i(a)^p) < 1$.
4. Distinct indices are separated modulo the maximal ideal: for $i \neq j$ some $a$ has $v(s_i(a) - s_j(a)) = 1$. This is the unramified condition.
5. Integers $r_i$ with $\operatorname{im} \varepsilon^L_i \cong R^{r_i}$.

Since the $\varepsilon^L_i$ split $R^g$, we have $\sum_i r_i = g$. Define
$$f_i = \sum_{n \geq 0} p^{-(n+1)}\, r_{\varphi^{n+1}(i)}.$$

### Sizes of torsion modules

A module $M$ over $R$ *has size* $x \in \mathbb{R}_{\geq 0}$ if $M \cong \bigoplus_k R/(c_k)$ for finitely many $c_k$ with $\prod_k v(c_k) = x$. For a finitely presented torsion module, $x$ is the absolute value of a generator of the zeroth Fitting ideal, so it does not depend on the decomposition. It is the multiplicative form of the [[length of a module|CZSCNZH8VY]]: a longer module has a smaller size.

For indices $i, j$ let $Q(i, j)$ be the quotient of $\operatorname{im}(\varepsilon^L_i)^{\mathsf T}$ by its intersection with $H_t(\operatorname{im} \varepsilon^T_j)$. This is the cokernel of the Hodge-Tate map from the $j$-eigenspace of $T$ to the $i$-eigenspace of the dual side.

### The statement

**Definition 2.8.1 (unramified cokernel length formula).** The *unramified cokernel length formula* is the following assertion. Let $p \neq 2$ and take a Hodge-Tate datum with an unramified eigen datum as above. Let $i$ be an index. If $Q(i, c(i))$ has size $V_1$ and $Q(c(i), i)$ has size $V_2$, then
$$V_1 = V_2 \cdot v(p)^{\,r_i/(p-1) - f_i}.$$

Lean: `ReciprocityTheory.PGsh.Up.UnramifiedCokernelLengthStatement`.

In additive form, with $\ell = -\log_{v(p)}$, the formula says $\ell(Q(i, c(i))) - \ell(Q(c(i), i)) = f_i - r_i/(p-1)$. If $\varphi$ fixes $i$, then $f_i = r_i/(p-1)$ and the two cokernels have the same size.

The proof uses two inputs. The first is a finite group that separates the embeddings.

**Definition 2.8.2 (separating group).** A *separating group* for the data is a finite commutative group $G$ with a map $\beta : G \to O$ such that $\rho \circ \beta$ is multiplicative with $\rho(\beta(1)) = 1$, the order of $G$ is a unit in $R$, and for all indices $i, k$ with $\varepsilon^T_i, \varepsilon^T_k \neq 0$:

1. $s_{\varphi(i)}(\beta\gamma) = s_i(\beta\gamma)^p$ for all $\gamma \in G$;
2. if $i \neq k$, some $\gamma$ has $v(s_i(\beta\gamma) - s_k(\beta\gamma)) = 1$;
3. some $\gamma$ has $v(s_i(\beta\gamma) - 1) = 1$.

The second input is the *Frobenius length bound*. Let $x_j = \varepsilon_j u_j$ be eigen-lifts of a basis of $N^\vee$ into $I$, such that the monomials in the $x_j$ with exponents below $p$ span $A$. For a block $\tau$ of indices let $L_\tau$ be the coefficient vectors supported on the lifts in block $\tau$. The bound says: if $N' \leq L_\tau$ is a submodule whose elements are the linear coefficients of functions in $I^2$, then $L_\tau / N'$ has size at most $v(p)^{r_\tau}$. The idea is that $I/I^2 \cong (R/p)^g$, and the $\tau$-block of it is $(R/p)^{r_\tau}$, of size $v(p)^{r_\tau}$.

### Reduction to the two inputs

**Theorem 2.8.3 (reduction to the Frobenius length bound).** Assume that every Hodge-Tate datum with an unramified eigen datum and $p \neq 2$ has a separating group, and that the Frobenius length bound holds. Then the unramified cokernel length formula holds.

Lean: `ReciprocityTheory.PGsh.Up.unramifiedCokernelLength_of_frobeniusLengthBound`.

*Proof.* Fix the data and the index $i$.

Step 1: averaging. Replace $B_t$ by $B'_t = \sum_k \varepsilon^L_k B_t \varepsilon^T_k$. The relation $B'^{\mathsf T}_t H_t - H_t^{\mathsf T} B'_t = c_p E$ still holds, because $H_t \varepsilon^T_k = (\varepsilon^L_{c(k)})^{\mathsf T} H_t$ and $(\varepsilon^T_k)^{\mathsf T} E = E \varepsilon^T_{c(k)}$. Now $B'_t$ commutes with the idempotents. Let $D$ be the $2g \times 2g$ matrix with rows $H_t$ and $B'_t$. Then $\det(D)^2 = c_p^{2g} \det E$, and $\det E$ is a unit, so $v(\det D) = v(c_p)^g$.

Step 2: block sizes. For each index $k$ let $X_k$ be the size of the cokernel of $D$ on the block $(k, c(k))$. The length identity gives
$$X_i \cdot V_1 = v(c_p)^{r_i} \cdot V_2.$$
The cokernel of $D$ is the direct sum of the blocks, so $\prod_k X_k = v(\det D) = v(c_p)^g$. In particular each $X_k$ is positive.

Step 3: the Frobenius inequality. The separating group gives elements of $O$ of order prime to $p$ whose eigenvalues separate the indices. From these one builds eigen-lifts $x_j = \varepsilon_j u_j$ in $I$, where $u_j$ reduces to a linear form and the product of $v(\varepsilon_j)$ over block $k$ is $X_k$. Since $\prod_k X_k = v(c_p)^g$, the monomials in the $x_j$ span $A$. The $p$-th power $x_j^p$ lies in $I^2$. Its linear part is supported on block $\varphi(k)$, and the determinant of these linear parts over block $k$ has size $X_k^p / X_{\varphi(k)}$. The Frobenius length bound, applied to the span of these linear parts, gives
$$X_k^p \leq X_{\varphi(k)} \cdot v(p)^{r_{\varphi(k)}}.$$

Step 4: solving. Write $X_k = v(p)^{y_k}$ with $y_k \geq 0$. Since $v(p) < 1$, Step 3 says $p\, y_k \geq y_{\varphi(k)} + r_{\varphi(k)}$. Iterate $n$ times:
$$y_k \geq \sum_{l=0}^{n-1} p^{-(l+1)} r_{\varphi^{l+1}(k)} + p^{-n} y_{\varphi^n(k)}.$$
The last term is nonnegative and tends to $0$, so $y_k \geq f_k$. Step 2 and $v(c_p)^{p-1} = v(p)$ give $\sum_k y_k = g/(p-1)$. Since $\varphi$ is a permutation and $\sum_k r_k = g$,
$$\sum_k f_k = \sum_{n \geq 0} p^{-(n+1)} \sum_k r_{\varphi^{n+1}(k)} = \frac{g}{p-1}.$$
So $y_k = f_k$ for all $k$. Substitute $X_i = v(p)^{f_i}$ and $v(c_p)^{r_i} = v(p)^{r_i/(p-1)}$ in Step 2 to get the formula. $\square$

### The separating group and the conclusion

**Theorem 2.8.4 (reduction to a separating group).** If every Hodge-Tate datum with an unramified eigen datum and $p \neq 2$ has a separating group, then the unramified cokernel length formula holds.

Lean: `ReciprocityTheory.PGsh.Up.frobenius_of_group` (also `ReciprocityTheory.PGsh.Up.u7F3`).

*Proof.* The Frobenius length bound holds, by the cotangent argument above. Apply the previous theorem. $\square$

**Theorem 2.8.5 (unramified cokernel length).** The unramified cokernel length formula holds. So for $p \neq 2$, a Hodge-Tate datum with an unramified eigen datum and an index $i$, the sizes of $Q(i, c(i))$ and $Q(c(i), i)$ satisfy $V_1 = V_2 \cdot v(p)^{\,r_i/(p-1) - f_i}$.

Lean: `ReciprocityTheory.PGsh.Up.u7` (also `ReciprocityTheory.PGsh.Up.embeddingSeparatingGroup`).

*Proof.* By the previous theorem it is enough to build a separating group. An integer $n$ prime to $p$ has $v(n) = 1$, so it is a unit in $R$. For each index $k$, and for each pair of distinct indices, choose an element $b$ of $O$ such that $\rho(b)$ has finite order $m$ prime to $p$ and the residues of the eigenvalues $s_k(b)$ do what is needed: they separate the two indices, or differ from $1$. Such elements exist because the residue field of $R$ is algebraically closed of characteristic $p$ and the eigenvalues are separated there by the unramified condition. Let $G$ be the product of the cyclic groups $\mathbb{Z}/m$ and let $\beta$ send the generators to the chosen elements. The order of $G$ is prime to $p$, so it is a unit. The eigenvalues of $\rho(\beta\gamma)$ are roots of unity of order prime to $p$, and the Frobenius condition on $\varphi$ then becomes an equality $s_{\varphi(i)}(\beta\gamma) = s_i(\beta\gamma)^p$. $\square$

**Remark 2.8.6 (Formalization).** The statement is `UnramifiedCokernelLengthStatement` ([UnramifiedCokernelLengthStatement.lean](lean:ReciprocityTheory/DualLattices/UnramifiedCokernelLengthStatement.lean#L45)), and the Hodge-Tate datum and setting are structures ([CotangentSurjective.lean](lean:ReciprocityTheory/DualLattices/CotangentSurjective.lean#L40)). The three theorems of this section are the last links of a chain of renamings ([FrobeniusOfGroupDivisorsRank.lean](lean:ReciprocityTheory/DualLattices/FrobeniusOfGroupDivisorsRank.lean#L34)): `unramifiedCokernelLength_of_frobeniusLengthBound` fills in `liftMonomialDeterminantStatement_holds` and `frobeniusBlock`, `frobenius_of_group` fills in `u7F3` ([SumX.lean](lean:ReciprocityTheory/DualLattices/SumX.lean#L11)), and `u7` fills in `embeddingSeparatingGroup` ([EmbeddingSeparatingGroup.lean](lean:ReciprocityTheory/DualLattices/EmbeddingSeparatingGroup.lean#L13)). Steps 1, 2 and 4 of the proof are in `unramifiedCokernelLength_of_length_eigenLengthProduct` ([UnramifiedCokernelLengthOfLengthEigenLengthProduct.lean](lean:ReciprocityTheory/DualLattices/UnramifiedCokernelLengthOfLengthEigenLengthProduct.lean#L208)), with the averaging step from `u1`. The size of a module is the predicate `HasLen`. The datum has projectors `P` and `PL`, but the eigen datum requires `P = 0` and `PL = 0`, so they play no part. The field `h5` of the datum only applies to $p = 2$, which the statement excludes. The auxiliary statements `EigenElementaryDivisorStatement` and `EigenRankStatement` carry no hypothesis $p \neq 2$. The material is local $p$-adic linear algebra, although the modules sit in a global chapter.
