---
title: The global reciprocity law
decls:
  - GroundTheory.Global.ideleSymbol_diagonal_and_ker_le
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The global reciprocity law

This section proves the [[Artin reciprocity|7938EKMMVR]] law for a finite abelian extension $L/K$ of [[number field|MWBDFS2KJ5]]s. The product of the local reciprocity maps over all places is a homomorphism from the idele group $I_K$ to $\operatorname{Gal}(L/K)$. We prove that it is trivial on the principal ideles $K^\times$, and that its kernel is $K^\times \cdot N_{L/K} I_L$. So it induces an isomorphism from $C_K/N_{L/K} C_L$ onto $\operatorname{Gal}(L/K)$, where $C_K$ is the [[idele class group|9GHD9MXNYV]]. The step [EveryCharacter from the Galois row](/step/every-character/) depends on this law. It is the form of [global class field theory](/learn/class-field-theory/#global-class-field-theory) that the later chapters use for abelian characters.

Throughout, $L/K$ is a Galois extension of number fields with abelian group $G = \operatorname{Gal}(L/K)$. For a place $v$ of $K$ we fix a place $w$ of $L$ above $v$. The [[decomposition group|7X92G8CQ33]] $G_w \leq G$ does not depend on $w$, because $G$ is abelian.

### The idele symbol

For a finite place $v$, [[local class field theory|SHEN158T3M]] gives the local reciprocity map $\theta_v : K_v^\times \to \operatorname{Gal}(L_w/K_v) = G_w \subseteq G$. It is trivial on the units $\mathcal{O}_{K_v}^\times$ if $v$ is unramified in $L$. For a real place $v$ that becomes complex in $L$, let $\theta_v(a)$ be complex conjugation at $w$ if $a < 0$ and the identity if $a > 0$. For every other infinite place, let $\theta_v$ be trivial.

**Definition 2.2.1 (idele symbol).** The *idele symbol* of $L/K$ is the homomorphism
$$\theta_{L/K} : I_K \to G, \qquad \theta_{L/K}(x) = \prod_{v \nmid \infty} \theta_v(x_v) \cdot \prod_{v \mid \infty} \theta_v(x_v).$$

Lean: `GroundTheory.Global.ideleSymbol`.

The product over the finite places is a finite product: for almost all $v$ the place $v$ is unramified in $L$ and $x_v$ is a unit, so the factor is $1$. The symbol is continuous, since it is trivial on an open subgroup of $I_K$. Each local map $\theta_v$ kills the local norms $N_{L_w/K_v} L_w^\times$. So $\theta_{L/K}$ kills the idele norms $N_{L/K} I_L$.

### The reciprocity law

**Theorem 2.2.2 (global reciprocity law).** Let $L/K$ be a Galois extension of number fields with abelian Galois group. Then:

1. $\theta_{L/K}(a) = 1$ for each $a \in K^\times$, embedded on the diagonal of $I_K$;
2. the kernel of $\theta_{L/K}$ is contained in $K^\times \cdot N_{L/K} I_L$.

Lean: `GroundTheory.Global.ideleSymbol_diagonal_and_ker_le`.

*Proof.* The idele symbol is defined place by place from $K$ and $L$, so it is unchanged under an isomorphism of the pair $(K, L)$. Choose an embedding of $L$ into a fixed algebraic closure $\overline{\mathbb{Q}}$ of $\mathbb{Q}$. Let $L'$ be its image and $K'$ the image of $K$. The maps $K \to K'$ and $L \to L'$ are isomorphisms of fields, compatible with the inclusions. So $L'/K'$ is Galois, and its group is again abelian: an element of $\operatorname{Gal}(L'/K')$ corresponds to an element of $\operatorname{Gal}(L/K)$, and a commutator maps to a commutator, which is $1$.

For finite extensions $K' \subseteq L'$ inside $\overline{\mathbb{Q}}$ the two statements are proved earlier, by abstract class field theory. The idele classes of the finite subextensions of $\overline{\mathbb{Q}}$ form a class formation for the absolute Galois group of $\mathbb{Q}$. The class formation gives an abstract reciprocity map
$$C_{K'}/N_{L'/K'} C_{L'} \xrightarrow{\ \sim\ } \operatorname{Gal}(L'/K').$$
On the class of an idele $x$ the abstract map agrees with $\theta_{L'/K'}(x)$. This agreement is proved first for cyclotomic extensions, where both maps can be computed, and then for all abelian extensions by a uniqueness argument. The abstract map is defined on idele classes, so $\theta_{L'/K'}$ kills $K'^\times$. Its kernel is the norm group of idele classes, so the kernel of $\theta_{L'/K'}$ on ideles is $K'^\times \cdot N_{L'/K'} I_{L'}$.

The isomorphisms $K \cong K'$ and $L \cong L'$ carry ideles to ideles, principal ideles to principal ideles, idele norms to idele norms and $\theta_{L/K}$ to $\theta_{L'/K'}$. So both statements transfer from $(K', L')$ to $(K, L)$. $\square$

**Corollary 2.2.3 (kernel of the idele symbol).** Let $L/K$ be as in the theorem. Then
$$\ker \theta_{L/K} = K^\times \cdot N_{L/K} I_L.$$

Lean: `GroundTheory.Global.ker_ideleSymbol`.

*Proof.* The theorem gives the inclusion $\subseteq$. The principal ideles are in the kernel by part 1 of the theorem, and the idele norms are in the kernel because each local symbol kills the local norms. $\square$

### The reciprocity map on idele classes

By part 1 of the theorem, $\theta_{L/K}$ factors through $C_K = I_K/K^\times$.

**Corollary 2.2.4 (reciprocity isomorphism).** Let $L/K$ be as in the theorem. The idele symbol induces a continuous surjective homomorphism $r_{L/K} : C_K \to G$ with kernel $N_{L/K} C_L$. So
$$C_K/N_{L/K} C_L \cong \operatorname{Gal}(L/K), \qquad [C_K : N_{L/K} C_L] = [L : K].$$

Lean: `GroundTheory.Global.reciprocityMapEquiv` (also `GroundTheory.Global.ker_reciprocityMap`, `GroundTheory.Global.index_range_ideleClassNorm_eq_finrank_of_isMulCommutative`).

*Proof.* The kernel of $r_{L/K}$ is the image of $K^\times \cdot N_{L/K} I_L$ in $C_K$, which is $N_{L/K} C_L$ by the previous corollary. The idele symbol is surjective. If not, its image lies in a proper subgroup $H$ of $G$ with $G/H$ cyclic and nontrivial. Let $F$ be the fixed field of $H$, a cyclic extension of $K$ with $[F:K] > 1$. The symbol of $F/K$ is the symbol of $L/K$ followed by restriction to $F$, so it is trivial on all of $I_K$. Then every idele is a local norm at each place, and so every idele class is a norm from $C_F$. The first inequality of the previous section gives $[F:K] \leq [C_K : N_{F/K} C_F] = 1$, a contradiction. The index is the order of $G$, which is $[L:K]$ since $L/K$ is Galois. $\square$

For a cyclic extension, the first inequality of the previous section now gives $\hat H^{-1}(C_L) = 0$. The reciprocity map is compatible with the [[Frobenius element|H5145REFMW]]s: for a finite place $v$ unramified in $L$, a uniformizer at $v$ maps to the Frobenius at $v$. This is the link between the idele symbol and the [splitting of primes](/learn/number-fields/#the-splitting-of-primes).

**Example 2.2.5.** Let $K = \mathbb{Q}$ and $L = \mathbb{Q}(\zeta_m)$, a [[cyclotomic field|NN77VYSGXR]]. For a prime $p$ not dividing $m$, the idele with $p$ at the place $p$ and $1$ elsewhere maps to the Frobenius $\zeta_m \mapsto \zeta_m^p$. The principal idele $p$ maps to $1$. So the product of the symbols at the other places is the inverse of the Frobenius, and this is the classical form of reciprocity for $\mathbb{Q}(\zeta_m)$.

**Remark 2.2.6 (Formalization).** The theorem is stated for abstract number fields $K$ and $L$ ([General.lean](lean:GroundTheory/GlobalFields/GlobalReciprocity/General.lean#L138)). Its proof chooses an embedding of $L$ into $\overline{\mathbb{Q}}$ by the lifting property of algebraically closed fields, so the embedding is not explicit. The results for subfields of $\overline{\mathbb{Q}}$ are in [RangeDiagonalLeKerIdeleSymbol.lean](lean:GroundTheory/GlobalFields/GlobalReciprocity/RangeDiagonalLeKerIdeleSymbol.lean#L163). The idele symbol is the product of the local symbols at the finite places, written as a product with finite support, and the symbols at the infinite places ([RangeIdeleNormLeKerIdeleSymbol.lean](lean:GroundTheory/GlobalFields/NormResidueSymbol/RangeIdeleNormLeKerIdeleSymbol.lean#L21)).
