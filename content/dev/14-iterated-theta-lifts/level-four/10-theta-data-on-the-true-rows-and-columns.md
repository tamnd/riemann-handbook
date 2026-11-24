---
title: Theta data on the true rows and columns
decls:
  - GlobalTheory.T.functionLevelData_of_equal_tuples_zero_intertwiners
  - GlobalTheory.Mem.RowsTies.rows_of_ties
  - GlobalTheory.ThetaRecordTrue.recFun_of_rows
  - GlobalTheory.ThetaRecordTrue.thEx_main
  - GlobalTheory.T.exists_thetaData_trueRowsColumns_allCompatible
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theta data on the true rows and columns

The last theorem of the previous section turns a record of functions with isometric rows into a theta datum with all ties. Here we build such a record. The rows are cusp forms that come from the multiplicity spaces of the tuples, and the theta kernels between consecutive rows realise the intertwiners of the multiplicity spaces. Then we apply the result to the true rows and columns of a column datum at level four. This gives the existence of a theta datum for each slot, which enters [the membership statement from the construction steps](/entry/member-e-closing-alt-alt/).

### Isometric rows and tied intertwiners

Let $D$ be the ambient datum. It has spaces $Y_0, \dots, Y_m$ of growing dimension, tuples $\mu$, and for each tuple and each $j \leq m$ a finite dimensional multiplicity space $M_{\mu, j}$ with an inner product. For $j < m$ it has an intertwiner $\iota_{\mu, j} : M_{\mu, j+1} \to M_{\mu, j}$. We write $\langle \cdot, \cdot \rangle$ for the inner products and $\mathcal{F}_j$ for a fundamental domain of the unitary group of $Y_j$.

**Definition 1.10.1 (Isometric rows and tied rows).** Let $\theta$ be the infinity family, $\psi$ the standard character of sign $-1$ and $W_f$ a Weil function for $\psi$. A record of functions $R$ has isometric rows on a set $U$ of tuples if for $\mu \in U$, $j \leq m$ and $x, y \in M_{\mu, j}$
$$\langle x, y \rangle = m_Y(\mu, j)\, c(Y_j) \int_{\mathcal{F}_j} \overline{R_{\mu, j}x(h)}\, R_{\mu, j}y(h)\, dh.$$
Here $R_{\mu, j} : M_{\mu, j} \to S(Y_j)$ is the row map into cusp forms, $m_Y$ is the multiplicity constant and $c(Y_j)$ the Petersson constant of $R$. The rows of $R$ are tied to $W_f$ if for each $\mu$, each $j < m$ and each $y \in M_{\mu, j+1}$ there is a function $L$ on the group of $Y_j$ such that
$$L(g) = m_Y(\mu, j{+}1)\, c(Y_{j+1}) \int_{\mathcal{F}_{j+1}} k_{\Phi_j}(h, g)\, R_{\mu, j+1}y(h)\, dh$$
for all $g$, with $k_{\Phi_j}$ the theta kernel of $W_f$ for the Schwartz function $\Phi_j$ of $R$, and such that for all $x \in M_{\mu, j}$
$$\langle \iota_{\mu, j}\, y, x\rangle = m_Y(\mu, j)\, c(Y_j) \int_{\mathcal{F}_j} \overline{L(g)}\, R_{\mu, j}x(g)\, dg.$$

So the theta lift of the row $j+1$ to $Y_j$, paired with the row $j$, computes the intertwiner. The record has characters $C$ and $\xi$ if its row characters and its character $\eta$ are those that the character frame $C$ and the Hecke characters $\xi$ give.

**Theorem 1.10.2 (Rows from tied tuples).** Assume rapid decay of cusp forms. Let $R$ be a real datum over a family of multiplicity spaces, whose level characters are those of the family, which has models and which forms a chain. Let $\xi$ be a family of Hecke characters of $E$, indexed by the tuples, each of finite order and trivial on the ideles of $F$. Let $U$ be a set of tuples and $t$ a map from tuples to the indices of the real datum. Assume for $\mu \in U$ that the Hecke character of $R$ at $t(\mu)$ is $\xi_\mu$, and that there are

- maps $e_j$ from $M_{\mu, j}$ into the spaces of $R$ at $t(\mu)$, for $j < m$, and a map $e_X$ from $M_{\mu, m}$ into the range of the top map at $t(\mu)$,
- quotient pairs $(\nu_j, \mathcal{F}_j)$ and constants $c_j > 0$ and $c_X > 0$, such that $e_j$ and $e_X$ scale the inner products by $c_j$ and $c_X$,
- a level $J$ and a character $\chi$ such that the range of the top map lies in the multiplicity space of level $J$ and character $\chi$,

and that the maps $e_j$ carry $\iota_{\mu, j}$ to the restriction maps of $R$, including the top step. Assume that $\iota_{\mu, j} = 0$ for $\mu \notin U$ and $j < m$. Then for each $\theta$, $\psi$ and $W_f$ as above there is a record of functions with characters $C$ and $\xi$, whose rows are tied to $W_f$, and whose rows are isometric on $U$.

Lean: `GlobalTheory.Mem.RowsTies.rows_of_ties` (also `GlobalTheory.T.functionLevelData_of_equal_tuples_zero_intertwiners`, a second name).

*Proof.* The infinity family and the standard character of sign $-1$ are unique, so $\theta$ and $\psi$ are those of the real datum. Since each $\xi_\mu$ has finite order and is trivial on $F$, there is a record $R_0$ whose row characters and whose character $\eta$ are those of $C$ and $\xi$. Characters are determined by their values, so $\eta$ of $R_0$ is $\eta$ of the real datum, and for $\mu \in U$ the row characters of $R_0$ are the level characters of $R$ at $t(\mu)$.

Now fix a tuple $\mu$. If $\mu \in U$, the theorem on isometric theta lifts for one tuple gives row maps into cusp forms, nonzero Schwartz functions $\Phi_j$ for $j < m$, the isometry, and the tie of rows for the constants $m_Y(\mu, j)\, c(Y_j)$. These constants are positive, since $m_Y$, the Petersson constants and the local factors are positive. If $\mu \notin U$, take the rows equal to $0$ and the Schwartz functions of $R_0$. The isometry on $U$ is empty for $\mu$. For the tie take $L = 0$: both integrals vanish, and $\iota_{\mu, j} = 0$ makes the left side $0$. Replace the rows and the Schwartz functions of $R_0$ by these choices. $\square$

### True rows and columns

Let $w$ be a column datum and $Z$ a later stage of $w$, with ambient datum $D = D(w, Z)$. A rows datum at $Z$ gives a real datum, a level, a tuple map and the characteristic data of the true rows. A choice datum $n$ gives Hecke characters $\xi$ of finite order, trivial on $F$. A tuple $\mu$ is used if it enters the true rows.

**Corollary 1.10.3 (Records on the true rows).** Assume rapid decay of cusp forms. Let $w$, $Z$, a rows datum and a choice datum $n$ be given, and assume that $\iota_{\mu, j} = 0$ for every tuple $\mu$ that is not used and every $j < m$. Then for each $\theta$, $\psi$ and $W_f$ there is a record of functions, with the characters of the column frame of $w$ at $Z$ and the characters $\xi$ of $n$, whose rows are tied to $W_f$ and isometric on the used tuples.

Lean: `GlobalTheory.ThetaRecordTrue.recFun_of_rows`.

*Proof.* The characterisation of weak real data gives the level characters, the models and the chain of the real datum. The weak compatibility theorem for real row sides on an adelic chain gives, for each used tuple, the maps $e_j$, $e_X$, the constants and the level of the previous theorem. The Hecke character of the real datum at $t(\mu)$ is $\xi_\mu$, by the tie of the tuples of the rows datum. This is the theorem on rows from tied tuples applied to these data and to $U$ the set of used tuples. $\square$

**Definition 1.10.4 (Theta datum for a slot).** Let $\mathcal{S}$ be a slot. A theta datum for a level four object $l$ of $\mathcal{S}$, at a column datum $w$ and a later stage $Z$, is a theta datum $X$ on $D(w,Z)$ with a provision and a complete tie $a$, whose Weil part is compatible with the equivariance, with a tied theta character datum for the column frame and the choice of $l$ whose characters are those of $a$, whose character $\psi$ is standard of sign $-1$, and whose rows are tied to the theta lifts. The slot has theta data if there is a column step from "pinned" to "each level four object has a theta datum" (column steps are defined in [Section 1.8.4](/entry/step-w-core/)).

**Theorem 1.10.5 (Theta data for a slot).** Assume the existence of the Weil representation for a unitary dual pair, rapid decay of cusp forms, the Casselman-Wallach theorem and the theory of Harish-Chandra modules. Assume that for each Harish-Chandra parameter $\lambda$ and signs $\varepsilon$ the group $U(J)$ has a discrete series representation with parameter $\lambda$, unique up to unitary equivalence, and that for each parameter of $U(p,q)$ there is a discrete series representation with that parameter. Let $\mathcal{S}$ be a slot, and assume that for every rows datum of $\mathcal{S}$ the intertwiners vanish on the tuples that are not used. Then $\mathcal{S}$ has theta data.

Lean: `GlobalTheory.ThetaRecordTrue.thEx_main` (also `GlobalTheory.T.exists_thetaData_trueRowsColumns_allCompatible`, a second name).

*Proof.* The statement is a column step, and we prove it for every context, base and column datum. Let $Z$ be a later stage and $l$ a level four object. The corollary on records on the true rows gives, for each $\theta$, $\psi$ and $W_f$, a record with isometric and tied rows. The theorem on a theta datum with all ties of [the previous section](/entry/exists-all-tied-eq-tied-on/) applies to it, with $U$ the set of used tuples. It gives $X$ with tied rows, a provision $A$ and a tie $a$, and a tied theta character datum whose characters agree with those of $a$. A tied Weil datum is compatible with the equivariance, and the agreement of characters gives the same characters. The character of the Weil tie is standard. $\square$

**Remark 1.10.6 (Formalization).** In [ExistsThetaDataTrueRowsColumnsAllCompatible.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsThetaDataTrueRowsColumnsAllCompatible.lean#L47) the hypotheses `CasselmanWallach` and `HarishChandraModules` are bound to `_` and are not used. The same proof drops the Petersson isometry of the theta datum (the `-` in the pattern), since the theta datum for a slot does not ask for it. The name of the second name says "allCompatible", but the conclusion is only the existence of a theta datum with the ties above. The column step starts from "pinned", but the proof does not use the pinned property. In [FunctionLevelDataOfEqualTuplesZeroIntertwiners.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/FunctionLevelDataOfEqualTuplesZeroIntertwiners.lean#L29) the tuples outside $U$ get the zero rows.
