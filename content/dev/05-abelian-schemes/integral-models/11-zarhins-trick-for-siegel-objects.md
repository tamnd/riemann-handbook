---
title: Zarhin's trick for Siegel objects
decls:
  - GlobalTheory.ZarhinFam.exists_zarhin_object
  - GlobalTheory.T.exists_principal_zarhin_object_of_siegKerBy
  - GlobalTheory.UPel.HT.exists_zarhin_data_siegKerBy
  - GlobalTheory.T.exists_zarhinTrick_family_siegel_kernelKilled
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Zarhin's trick for Siegel objects

This section proves result 6 of the section on the Siegel problem with kernel killed by $d$: a Siegel object of genus $h$ whose kernel is killed by $d$ is a direct factor of a principal Siegel object of genus $8h$ with an action of an order, and this principal object is unique up to a map with actions. The construction is Zarhin's trick over a base. Classically, if $\mu : A \to A^\vee$ is a polarization of an abelian variety, then $(A \times A^\vee)^4$ has a principal polarization ([Zarhin's trick](/learn/abelian-varieties/#polarizations-and-zarhins-trick)). Here we take the product $A^4 \times B^4$, where $B$ plays the role of the dual. The theorem is used in the proof of the [representability of the Siegel problem](/entry/sd-rep-of-coprime/), with $h' = 8h$. We keep the notation of the earlier sections: Siegel objects $c = (A, P, \lambda)$ (Definition 8.1.5), principal Siegel objects (Definition 8.3.2), right actions with the Rosati condition and maps with actions (Definition 8.7.2), and Zarhin data and the Zarhin relation (Definition 8.7.4). Throughout, $h \geq 1$, $M \geq 3$ is odd, $d > 0$ and $\gcd(M, d) = 1$.

### The Zarhin order

By Lagrange's four-square theorem, $d - 1 = a^2 + b^2 + c^2 + e^2$ for some integers. The matrix of left multiplication by the quaternion $a + bi + cj + ek$ is a matrix $\alpha \in M_4(\mathbb{Z})$ with $\alpha^{T} \alpha = \alpha \alpha^{T} = (d - 1) \cdot 1$. We fix such an $\alpha$. We index $8 \times 8$ matrices by $\{1, 2, 3, 4\} \sqcup \{1', 2', 3', 4'\}$ and write them in $4 \times 4$ blocks.

**Definition 8.11.1 (Zarhin order).** Put

$$F = \begin{pmatrix} 1 & \alpha^{T} \\ \alpha & d \cdot 1 \end{pmatrix}, \qquad F^{-1} = \begin{pmatrix} d \cdot 1 & -\alpha^{T} \\ -\alpha & 1 \end{pmatrix}.$$

The *Zarhin order* $O_d$ is the set of $N \in M_8(\mathbb{Z})$ whose lower left block is divisible by $d$, that is, $d \mid N_{i' j}$ for all $i, j \in \{1, \dots, 4\}$. For $N \in O_d$ put $\bar{N} = F N^{T} F^{-1}$. Let $E \in O_d$ be the matrix unit at $(1, 1)$, and for $k = 1, \dots, 8$ let $o_k \in O_d$ be the matrix unit at $(1, \sigma(k))$, where $\sigma(1), \dots, \sigma(8)$ is $1, 2, 3, 4, 1', 2', 3', 4'$.

Lean: `GlobalTheory.ZarhinFam.ord` (also `GlobalTheory.ZarhinFam.bar`, `GlobalTheory.ZarhinFam.idem`, `GlobalTheory.ZarhinFam.oMat`, `GlobalTheory.ZarhinFam.form`).

The product $F F^{-1}$ has blocks $d - \alpha^{T}\alpha = 1$, $0$, $0$ and $d - \alpha \alpha^{T} = 1$, so $F^{-1}$ is the inverse of $F$, and $\det F = 1$. The set $O_d$ is a subring of $M_8(\mathbb{Z})$: in a product $N N'$, each term of a lower left entry has a factor from a lower left block. The map $N \mapsto \bar{N}$ is additive, it preserves $O_d$, and it is an involution, since $F$ and $F^{-1}$ are symmetric. The matrix $E$ is idempotent. The ring $O_d$ is a free abelian group of rank 64, and we use the following fact.

1. (An order datum.) There are $e_1, \dots, e_r \in O_d$ that span $O_d$ as an abelian group, a matrix $W \in M_r(\mathbb{Z})$ with $W + W^{T}$ positive definite and an integer $d_0 > 0$ with $\sum_{i, j} W_{ij} e_j \bar{e}_i = d_0$.

So $(O_d, N \mapsto \bar{N}, e_1, \dots, e_r, W, d_0)$ is an order datum (Definition 8.7.1).

### The Zarhin object

Let $c = (A, P, \lambda)$ be a Siegel object of genus $h$ over $t : S \to \operatorname{Spec} B_M$ with kernel killed by $d$, where $d$ is a unit on $S$. We use the following input.

2. (A complementary isogeny.) There are an abelian scheme $B$ over $S$, a line bundle $Q$ on $A \times_S B$ and maps of group schemes $\lambda_B : A \to B$ and $\mu : B \to A$ with these properties: $B$ is a [[dual abelian scheme|HZXSESHC8P]] of $A$ with Poincaré bundle $Q$, and $A$ is a dual of $B$ with Poincaré bundle $\sigma^* Q$; $\mu \lambda_B = d$ on $A$ and $\lambda_B \mu = d$ on $B$; and $P \cong (1 \times \lambda_B)^* Q$.

So $\lambda_B$ is the polarization of $c$ ([duality and the Poincaré bundle](/learn/abelian-varieties/#duality-and-the-poincar-bundle)), and $\mu$ exists because $d$ kills its kernel.

**Definition 8.11.2 (Zarhin object).** Let $Z = A^4 \times_S B^4$, an abelian scheme over $S$. Write a point of $Z$ as $(a, b) = (a_1, \dots, a_4, b_1, \dots, b_4)$.

- For $N \in O_d$, the endomorphism $[N]$ of $Z$ sends $(a, b)$ to $(a', b')$ with
$$\begin{aligned} a'_i &= \textstyle\sum_j N_{ji}\, a_j + \sum_j \tfrac{N_{j' i}}{d}\, \mu(b_j), \\ b'_i &= \textstyle\sum_j N_{j i'}\, \lambda_B(a_j) + \sum_j N_{j' i'}\, b_j. \end{aligned}$$
- The maps $\iota : A \to Z$ and $q : Z \to A$ are $\iota(x) = (x, 0, 0, 0; 0, 0, 0, 0)$ and $q(a, b) = a_1$.
- The line bundle $P_Z$ on $Z \times_S Z$ is a line bundle in the class
$$\begin{aligned} &\textstyle\sum_i (a_i, a'_i)^* P + \sum_{i, j} \alpha_{ji} (a_i, b'_j)^* Q \\ &\textstyle\quad + \sum_{i, j} \alpha_{ji} (a'_i, b_j)^* Q + \sum_j (\mu(b'_j), b_j)^* Q \end{aligned}$$
in $\operatorname{Pic}(Z \times_S Z)$, where $((a, b), (a', b'))$ is a point of $Z \times_S Z$.
- For an additive map $\kappa = (\kappa_1, \dots, \kappa_8)$ from $\mathbb{Z}^{16h}$ to $(\mathbb{Z}^{2h})^8$, the level map is $\lambda_Z(a) = \sum_{k=1}^{8} [o_k]\, \iota\, \lambda(\kappa_k(a))$ for $a \in \mathbb{Z}^{16h}$.

Lean: `GlobalTheory.ZarhinFam.Zob` (also `GlobalTheory.ZarhinFam.actZ`, `GlobalTheory.ZarhinFam.incZ`, `GlobalTheory.ZarhinFam.prZ`, `GlobalTheory.ZarhinFam.zP`, `GlobalTheory.ZarhinFam.levZ`).

The formula for $[N]$ is the product of the row $(a, b)$ with the matrix $N$, where an entry of the lower left block acts through $\mu / d$ and an entry of the upper right block acts through $\lambda_B$. So $[N N'] = [N'][N]$, and $N \mapsto [N]$ is a right action. The first term of the class of $P_Z$ is the bundle $P$ on each factor $A$, and the coefficients $\alpha_{ji}$ and the last term put the blocks $\alpha$, $\alpha^{T}$ and $d$ of $F$ into the other entries.

We also fix the map $\jmath : \mathbb{Z}^{2h} = \mathbb{Z}^{h} \oplus \mathbb{Z}^{h} \to \mathbb{Z}^{8h} \oplus \mathbb{Z}^{8h}$ that puts a vector into the first $h$ coordinates of each summand and $0$ into the others. Let $\langle \cdot, \cdot \rangle$ be the standard symplectic form of Definition 8.1.5.

3. (Symplectic transfer.) There are additive maps $\kappa_1, \dots, \kappa_8 : \mathbb{Z}^{16h} \to \mathbb{Z}^{2h}$ with these properties: for all $a, b \in \mathbb{Z}^{16h}$,
$$\textstyle\sum_{k, l = 1}^{8} F_{\sigma(k) \sigma(l)} \langle \kappa_k(a), \kappa_l(b) \rangle \equiv \langle a, b \rangle \pmod M;$$
and $\kappa_1(\jmath(a)) = a$ and $\kappa_k(\jmath(a)) = 0$ for $k \neq 1$, for all $a \in \mathbb{Z}^{2h}$.

4. (The Zarhin object is a principal Siegel object.) With $\kappa$ as in result 3, the data $(Z, P_Z, \lambda_Z)$ form a principal Siegel object of genus $8h$ over $t$. The map $N \mapsto [N]$ is a right action of $O_d$ on $Z$ with the Rosati condition for $P_Z$. The maps $\iota$ and $q$ are maps of group schemes with $q \iota = 1$, $\iota q = [E]$ and $\iota \lambda(a) = \lambda_Z(\jmath(a))$, and $P \cong (\iota \times \iota)^* P_Z$.

Some parts of result 4 can be checked by hand. By the formula for $[N]$, the endomorphism $[E]$ sends $(a, b)$ to $(a_1, 0, 0, 0; 0, 0, 0, 0)$, which is $\iota q$. Result 3 gives $\lambda_Z(\jmath(a)) = [o_1] \iota \lambda(a) = [E] \iota \lambda(a) = \iota \lambda(a)$. On $\iota(A) \times \iota(A)$ only the term $(a_1, a'_1)^* P$ of the class of $P_Z$ survives, so $(\iota \times \iota)^* P_Z \cong P$. The other parts need the theory of the Poincaré bundle, and we only indicate the ideas. The congruence in result 3 is the condition that the Weil pairing of $\lambda_Z$ is the standard one. The fact $\det F = 1$ is behind the principality of $P_Z$, as in the classical trick. For the bilinear form $(x, y) \mapsto x F y^{T}$ on row vectors, $\bar{N}$ is the adjoint of $N$: $(x N) F y^{T} = x F (y \bar{N})^{T}$, since $F$ is symmetric. This is behind the Rosati condition.

**Theorem 8.11.3 (Principal Zarhin objects).** Let $h \geq 1$, let $M \geq 3$ be odd, and let $d > 0$ with $\gcd(M, d) = 1$. Then there are an additive map $\jmath : \mathbb{Z}^{2h} \to \mathbb{Z}^{16h}$, an integer $n$, elements $o_1, \dots, o_n \in O_d$ and additive maps $\kappa_1, \dots, \kappa_n : \mathbb{Z}^{16h} \to \mathbb{Z}^{2h}$ with the following property. For every scheme $S$, every $t : S \to \operatorname{Spec} B_M$ with $d$ a unit on $S$, and every Siegel object $c$ of genus $h$ and level $M$ over $t$ with kernel killed by $d$, there are a principal Siegel object $z$ of genus $8h$ and level $M$ over $t$ and a right action $N \mapsto [N]$ of $O_d$ on $z$ with the Rosati condition for $N \mapsto \bar{N}$ such that $z$ is Zarhin related to $c$ for the idempotent $E$, the map $\jmath$, the $o_k$ and the $\kappa_k$.

Lean: `GlobalTheory.ZarhinFam.exists_zarhin_object` (also `GlobalTheory.T.exists_principal_zarhin_object_of_siegKerBy`, a second name).

The Zarhin relation (Definition 8.7.4) uses only the ring, the idempotent, $\jmath$, the $o_k$ and the $\kappa_k$, so it makes sense here before an order datum is chosen. The data $\jmath$, $n$, $o_k$ and $\kappa_k$ do not depend on $S$ or $c$.

*Proof.* Take $\kappa_1, \dots, \kappa_8$ from result 3, $n = 8$, $\jmath$ as above and $o_k$ the matrix units of the definition. Let $S$, $t$ and $c$ be given. Result 2 gives $B$, $Q$, $\lambda_B$ and $\mu$, and we form the Zarhin object $z = (Z, P_Z, \lambda_Z)$ with the action $N \mapsto [N]$. By result 4, $z$ is a principal Siegel object of genus $8h$ over $t$, and the action is a right action with the Rosati condition. We check the four clauses of the Zarhin relation with the maps $\iota$ and $q$. Clauses 1 to 3 are the last part of result 4. Clause 4, $\lambda_Z(a) = \sum_k [o_k] \iota \lambda(\kappa_k(a))$, is the definition of $\lambda_Z$. $\square$

### Zarhin's trick

We use one more input.

5. (Uniqueness.) Let $\jmath$, $o_1, \dots, o_n$ and $\kappa_1, \dots, \kappa_n$ be any data as in the theorem. Let $c$ be a Siegel object of genus $h$ over $t : S \to \operatorname{Spec} B_M$ with kernel killed by $d$, where $d$ is a unit on $S$. Let $z_1$ and $z_2$ be principal Siegel objects of genus $8h$ over $t$ with right actions of $O_d$ with the Rosati condition for $N \mapsto \bar{N}$, both Zarhin related to $c$ for $E$, $\jmath$, the $o_k$ and the $\kappa_k$. Then there is a map from $z_1$ with its action to $z_2$ with its action over the identity of $S$.

**Theorem 8.11.4 (Zarhin's trick for Siegel objects).** Let $h \geq 1$, let $M \geq 3$ be odd, and let $d > 0$ with $\gcd(M, d) = 1$. Then there is a Zarhin datum $(O, a \mapsto \bar{a}, e_1, \dots, e_r, W, d_0, e, \jmath, o_1, \dots, o_n, \kappa_1, \dots, \kappa_n)$ with $h' = 8h$ and the following two properties.

- (a) For every scheme $S$, every $t : S \to \operatorname{Spec} B_M$ with $d$ a unit on $S$, and every Siegel object $c$ of genus $h$ over $t$ with kernel killed by $d$, there are a principal Siegel object $z$ of genus $8h$ over $t$ and a right action of $O$ on $z$ with the Rosati condition such that $z$ is Zarhin related to $c$.
- (b) Let $S$, $t$ and $c$ be as in (a). Let $z_1$ and $z_2$ be principal Siegel objects of genus $8h$ over $t$ with right actions of $O$ with the Rosati condition, both Zarhin related to $c$. Then there is a map from $z_1$ with its action to $z_2$ with its action over the identity of $S$.

Lean: `GlobalTheory.UPel.HT.exists_zarhin_data_siegKerBy` (also `GlobalTheory.T.exists_zarhinTrick_family_siegel_kernelKilled`, a second name).

*Proof.* Take $O = O_d$ with the map $N \mapsto \bar{N}$, which is additive, and take $e_1, \dots, e_r$, $W$ and $d_0$ from result 1. Take $e = E$, which is idempotent, and take $\jmath$, $n$, the $o_k$ and the $\kappa_k$ from the previous theorem. Then we have a Zarhin datum. Property (a) is the previous theorem. Property (b) is result 5, which holds for every choice of $\jmath$, $o_k$ and $\kappa_k$, so in particular for ours. $\square$

The classical form of the trick is due to Zarhin: for an abelian variety $A$ over a field, $(A \times A^\vee)^4$ has a principal polarization (Yu. G. Zarhin, *A remark on endomorphisms of abelian varieties over function fields of finite characteristic*, Math. USSR-Izv. 8 (1974)). A form over a base is in L. Moret-Bailly, *Pinceaux de variétés abéliennes*, Astérisque 129 (1985), Chapitre IX.

**Remark 8.11.5 (Formalization).** The matrix $\alpha$ is chosen from an existence statement and is not given by a formula: [FormMulTransposeMulFormInvMem.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FormMulTransposeMulFormInvMem.lean#L10). The four-square construction above is ours. The involution property of $N \mapsto \bar{N}$ is proved only for $d > 0$, and the order datum asks only that this map is additive: [FormMulTransposeMulFormInvMem.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FormMulTransposeMulFormInvMem.lean#L90). The line bundle $P_Z$ is chosen by choice from its class in the Picard group: [KappaOK.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KappaOK.lean#L73). The level map $\lambda_Z$ is defined by the formula of clause 4, so clause 4 holds by definition: [KappaOK.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KappaOK.lean#L87) and [ExistsZarhinObject.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsZarhinObject.lean#L44). We did not unfold the condition that $B$ is a dual of $A$ with Poincaré bundle $Q$, and we state result 2 only as far as we read it: [KappaOK.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KappaOK.lean#L92). The uniqueness result 5 is stated for every $\jmath$, $o_k$ and $\kappa_k$, not only for the data of the theorem: [ZarhinTrickPrincipalObjectsIsoUniqueStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ZarhinTrickPrincipalObjectsIsoUniqueStatement.lean#L8). The second name of the theorem on principal Zarhin objects is a wrapper that tries several forms of one proof term under a raised heartbeat limit: [ExistsZarhinObjectStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsZarhinObjectStatement.lean#L7). We read the statements of results 1 to 5, not their proofs, and the explanations of result 4 given above are ours.
